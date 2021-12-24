"""Views."""

import os
from flask import Blueprint, request
from flask.views import MethodView
from sqlalchemy.sql import func, select

from . import schemas as user_schemas
from . import service as user_service
from ...tools.flasgger_marshmallow import swagger_decorator
from ...session import session_scope


user_blueprint = Blueprint('user', __name__)

class UserCurrentGet(MethodView):
    """Get user current."""

    @swagger_decorator(response_schema={200: user_schemas.UserResponseSchema})
    def get(self):
        """Get user info."""
        user = user_service.get_user()
        return user

user_blueprint.add_url_rule('/current', view_func=UserCurrentGet.as_view("user_current_api"))