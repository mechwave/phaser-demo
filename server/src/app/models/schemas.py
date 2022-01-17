from inspect import Parameter
from marshmallow import fields, EXCLUDE
from flask_marshmallow import Schema
from .map import User, Game, Unit, Building


class UserSchema(Schema):
    """User response data."""

    id = fields.String(doc='User ID')
    name = fields.String(doc='Username')

    class Meta:
        """Meta."""

        strict = True
        unknown = EXCLUDE

class UnitParameterSchema(Schema):
    """Parameter data."""

    unit_id = fields.String(doc='Unit ID')
    name = fields.String(doc='Unit name')
    description = fields.String(doc='Description')
    value = fields.String(doc='Value')

    class Meta:
        """Meta."""

        strict = True
        unknown = EXCLUDE

class UnitSchema(Schema):
    """Unit data."""

    id = fields.String(doc='Unit ID')
    game_id = fields.String(doc='Game ID')
    name = fields.String(doc='Username')
    description = fields.String(doc='Description')
    parameters = fields.List(fields.Nested(UnitParameterSchema), doc='Unit parameters')

    class Meta:
        """Meta."""

        strict = True
        unknown = EXCLUDE

class GameSchema(Schema):
    """Game data."""

    id = fields.String(doc='Game ID')
    name = fields.String(doc='Username')
    description = fields.String(doc='Description')
    max_players = fields.Integer(doc='Max players count.')
    units = fields.List(fields.Nested(UnitSchema), doc='Units list')
    buildings = fields.List(fields.Nested(Building), doc='Buildings list')

    class Meta:
        """Meta."""

        strict = True
        unknown = EXCLUDE