"""Session."""

from contextlib import contextmanager

from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.orm.session import Session as SessionSQLA

Session = sessionmaker()


@contextmanager
def session_scope(session: SessionSQLA = Session) -> SessionSQLA:
    """Provide a transactional scope around a series of operations."""
    db_uri = current_app.config.get('DB_URI', '')
    session.configure(bind=create_engine(db_uri, client_encoding='utf8', poolclass=NullPool))
    sess = session()
    try:
        yield sess
        sess.commit()
    except:
        sess.rollback()
        raise
    finally:
        sess.invalidate()
