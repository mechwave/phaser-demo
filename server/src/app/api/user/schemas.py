"""Schemas."""

from marshmallow import fields, EXCLUDE
from flask_marshmallow import Schema


class UserResponseSchema(Schema):
    """User response data."""
    id = fields.String(doc='User ID')
    name = fields.String(doc='Username')

    class Meta:
        """Meta."""

        strict = True
        unknown = EXCLUDE