"""Apis."""

from ..tools.common import BlueprintContainer
from .user import user_blueprint
from .index import index_blueprint
blueprints = [BlueprintContainer(index_blueprint, "/"),]

blueprints.append(BlueprintContainer(user_blueprint, "/api/user"))