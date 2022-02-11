
import os
from flask import Blueprint, request
from flask.views import MethodView
from sqlalchemy.sql import func, select

#from ...models import schemas as base_schemas
from .schemas import MapTileSchema, TilesListSchema
from . import service as map_service
from ...tools.flasgger_marshmallow import swagger_decorator
from ...session import session_scope


map_blueprint = Blueprint('map', __name__)

class RandomMap(MethodView):
    """Get game info."""

    @swagger_decorator(response_schema={200: TilesListSchema}, tag_name = "Map")
    def get(self):
        """Get random map."""
        tiles, MAX_X, MAX_Y = map_service.get_random_map()
        result = MapTileSchema().dump(tiles, many=True)
        return {
            "tiles": result,
            "tile_size": 40,
            "width": MAX_X,
            "height": MAX_Y
            }

map_blueprint.add_url_rule('/random', view_func=RandomMap.as_view("random_map"))