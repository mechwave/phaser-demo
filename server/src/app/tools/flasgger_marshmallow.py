"""Flasgger marshmallow."""

import functools

import marshmallow
import yaml
from flask import request
from marshmallow import fields
from marshmallow.utils import _Missing


FIELDS_JSON_TYPE_MAP = {
    fields.Nested: 'object',
    fields.Dict: 'object',
    fields.List: 'array',
    fields.String: 'string',
    fields.UUID: 'string',
    fields.Number: 'number',
    fields.Integer: 'number',
    fields.Decimal: 'number',
    fields.Boolean: 'bool',
    fields.Float: 'number',
    fields.DateTime: 'string',
    fields.Time: 'string',
    fields.Date: 'string',
    fields.TimeDelta: 'number',
    fields.Url: 'string',
    fields.URL: 'string',
    fields.Email: 'string',
    fields.Str: 'string',
    fields.Bool: 'bool',
    fields.Int: 'number',
}

if int(marshmallow.__version__.split('.')[1]) == 3:
    FIELDS_JSON_TYPE_MAP.update({
        fields.NaiveDateTime: 'string',
        fields.AwareDateTime: 'string',
        fields.Tuple: 'array',
    })


def unpack(value):
    """Return a three tuple of data, code, and headers."""
    if not isinstance(value, tuple):
        return value, 200, {}

    try:
        data, code, headers = value
        return data, code, headers
    except ValueError:
        pass

    try:
        data, code = value
        return data, code, {}
    except ValueError:
        pass

    return value, 200, {}


def swagger_decorator(
        path_schema=None, query_schema=None,
        form_schema=None, json_schema=None,
        headers_schema=None, response_schema=None, tag_name = 'default'
):
    def decorator(func):

        def parse_simple_schema(c_schema, location):
            ret = []
            for key, value in c_schema.__dict__.get('_declared_fields').items():
                values_real_types = list(set(FIELDS_JSON_TYPE_MAP) & set(value.__class__.__mro__))
                values_real_types.sort(key=value.__class__.__mro__.index)
                if not values_real_types:
                    raise 'Неподдерживаемый тип ' % str(type(value))
                tmp = {
                    'in': location,
                    'name': getattr(value, 'data_key', None) or key,
                    'type': FIELDS_JSON_TYPE_MAP.get(values_real_types[0]),
                    'required': value.required if location != 'path' else True,
                    'description': value.metadata.get('doc', '')
                }
                if not isinstance(value.default, _Missing):
                    tmp['default'] = value.default
                ret.append(tmp)
            return ret

        def parse_json_schema(r_s):
            tmp = {}
            for key, value in (
                    r_s.__dict__.get('_declared_fields') or r_s.__dict__.get('declared_fields') or {}).items():
                key = getattr(value, 'data_key', None) or key
                if isinstance(value, fields.Nested):
                    if value.many:
                        tmp[key] = {
                            'type': 'array',
                            'description': value.metadata.get('doc', ''),
                            'items': {
                                'type': 'object',
                                'properties': parse_json_schema(value.schema),
                            }
                        }
                    else:
                        tmp[key] = {
                            'type': 'object',
                            'properties': parse_json_schema(value.schema)
                        }
                elif isinstance(value, fields.List):
                    tmp[key] = {
                        'type': 'array',
                        'description': value.metadata.get('doc', ''),
                        'items': {
                            'type': 'string',
                        }
                    }
                    if not isinstance(value.default, _Missing):
                        tmp[key]['default'] = value.default
                else:
                    values_real_types = list(set(FIELDS_JSON_TYPE_MAP) & set(value.__class__.__mro__))
                    values_real_types.sort(key=value.__class__.__mro__.index)
                    if not values_real_types:
                        raise 'Неподдерживаемый тип ' % str(type(value))
                    tmp[key] = {
                        'type': FIELDS_JSON_TYPE_MAP.get(values_real_types[0]),
                        'description': value.metadata.get('doc', ''),
                        'required': value.required,
                    }
                    if not isinstance(value.default, _Missing):
                        tmp[key]['default'] = value.default
            return tmp

        def parse_request_body_json_schema(c_schema):
            tmp = {
                'in': 'body',
                'name': 'body',
                'required': True,
                'description': 'json body',
                'schema': {
                    'properties': parse_json_schema(c_schema),
                    'type': 'object',
                }
            }
            return [tmp]

        def generate_doc():
            doc_dict = {}

            if path_schema or query_schema or form_schema or json_schema or headers_schema:

                doc_dict['parameters'] = []
            if path_schema:
                doc_dict['parameters'].extend(parse_simple_schema(path_schema, 'path'))
            if query_schema:
                doc_dict['parameters'].extend(parse_simple_schema(query_schema, 'query'))
            if form_schema:
                doc_dict['parameters'].extend(parse_simple_schema(form_schema, 'formData'))
            if headers_schema:
                doc_dict['parameters'].extend(parse_simple_schema(headers_schema, 'header'))
            if json_schema:
                doc_dict['parameters'].extend(parse_request_body_json_schema(json_schema))
            if response_schema:
                doc_dict['responses'] = {}
                for code, current_schema in response_schema.items():
                    doc_dict['responses'][code] = {
                        'description': current_schema.__doc__,
                        'schema': {
                            'type': 'object',
                            "properties": parse_json_schema(current_schema),
                        },
                    }
                    if not doc_dict['responses'][code].get('schema', {}).get('properties'):
                        doc_dict['responses'][code].update({'schema': None})
                    if getattr(current_schema.Meta, 'headers', None):
                        doc_dict['responses'][code].update(
                            {'headers': parse_json_schema(current_schema.Meta.headers)}
                        )
                    produces = getattr(current_schema.Meta, 'produces', None)
                    if produces:
                        doc_dict.setdefault('produces', [])
                        doc_dict['produces'].extend(produces)
                        'application/xml' in produces and doc_dict['responses'][code]['schema'] and \
                        doc_dict['responses'][code]['schema'].update(
                            {'xml': {'name': getattr(current_schema.Meta, 'xml_root', 'xml')}}
                        )
            doc_dict['tags'] = [tag_name]
            ret_doc = """---\n""" + yaml.dump(doc_dict)
            return ret_doc

        func.__doc__ = (func.__doc__.strip() + generate_doc()) if func.__doc__ else generate_doc()

        @functools.wraps(func)
        def wrapper(*args, **kw):
            path_params = request.view_args
            query_params = request.args
            form_params = request.form
            json_params = request.get_json(silent=True) or {}
            header_params = request.headers
            request.path_schema, request.path_schema, request.form_schema = [None] * 3
            request.json_schema, request.headers_schema = [None] * 2
            try:
                path_schema and setattr(request, 'path_schema', path_schema().load(path_params or {}))
                query_schema and setattr(request, 'query_schema', query_schema().load(query_params or {}))
                form_schema and setattr(request, 'form_schema', form_schema().load(form_params or {}))
                json_schema and setattr(request, 'json_schema', json_schema().load(json_params or {}))
                headers_schema and setattr(request, 'headers_schema', headers_schema().load(dict(header_params)))
            except Exception as e:
                return 'request error: %s' % ''.join(
                    [('%s: %s; ' % (x, ''.join(y))) for x, y in e.messages.items()]), 400
            f_result = func(*args, **kw)
            data, code, headers = unpack(f_result)
            try:
                if response_schema and response_schema.get(code):
                    data = response_schema.get(code)().load(data or {})
                    r_headers_schema = getattr(response_schema.get(code).Meta, 'headers', None)
                    if r_headers_schema:
                        headers = r_headers_schema().load(headers or {})
            except Exception as e:
                return 'response error: %s' % ''.join(
                    [('%s: %s; ' % (x, ''.join(y))) for x, y in e.messages.items()]), 400
            return data, code, headers

        return wrapper

    return decorator
