"""WSGI runner."""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import get_app
from setting import ProdConfig

app = get_app(ProdConfig)

def application(environ, start_response):
    """WSGI application."""
    return app(environ, start_response)
