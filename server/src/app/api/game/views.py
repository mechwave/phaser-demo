
import os
from flask import Blueprint, request
from flask.views import MethodView
from sqlalchemy.sql import func, select

from ...models import schemas as base_schemas
from . import service as game_service
from ...tools.flasgger_marshmallow import swagger_decorator
from ...session import session_scope


game_blueprint = Blueprint('game', __name__)

class Game(MethodView):
    """Get game info."""

    @swagger_decorator(response_schema={200: base_schemas.GameSchema}, tag_name = "Game")
    def get(self):
        """Get game info."""
        with session_scope() as session:
            game = game_service.get_games_list(session = session, user_id=1)
            result = base_schemas.GameSchema().dump(game)
        return result

game_blueprint.add_url_rule('/current', view_func=Game.as_view("game_api"))