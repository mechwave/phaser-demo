import os
import uuid
import datetime
from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import MetaData, Table, Column, select, and_, or_, not_, func, text
from sqlalchemy.orm import load_only
from ...models.map import User

def get_user():
  """Get user."""
  return {"id": "0", "name":"current_user"}