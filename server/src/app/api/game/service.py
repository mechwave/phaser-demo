import os
import uuid
import datetime
from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import MetaData, Table, Column, select, and_, or_, not_, func, text
from sqlalchemy.orm import load_only
from ...models.map import User, Game

def get_games_list(session: Session, user_id: int):
    """Get games list for user."""
    try:
        games = session.query(Game).filter(Game.user_id == user_id).one()
        return games
    except Exception as e:
        return None