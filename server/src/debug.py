"""Debuger."""

from app import get_app
from debug_setting import DevConfig

app = get_app(DevConfig)

from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
