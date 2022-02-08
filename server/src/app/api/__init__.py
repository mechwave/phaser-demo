"""Apis."""

from ..tools.common import BlueprintContainer
from .user import user_blueprint
from .game import game_blueprint
from .maps import map_blueprint
from .index import index_blueprint
blueprints = [BlueprintContainer(index_blueprint, "/"),]
blueprints.append(BlueprintContainer(user_blueprint, "/api/user"))
blueprints.append(BlueprintContainer(game_blueprint, "/api/game"))
blueprints.append(BlueprintContainer(map_blueprint, "/api/map"))
