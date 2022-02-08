from inspect import Parameter
from marshmallow import fields, EXCLUDE
from flask_marshmallow import Schema


class MapTileSchema(Schema):
    """Tile schema."""

    x = fields.Integer(doc='x coordinate')
    y = fields.Integer(doc='y coordinate')
    terrain = fields.String(doc='Terrain type')
    class Meta:
        """Meta."""

        strict = True
        unknown = EXCLUDE

class TilesListSchema(Schema):
    """Tiles list schema."""

    tiles = fields.Nested(MapTileSchema, many=True, doc ="Tiles list.")
