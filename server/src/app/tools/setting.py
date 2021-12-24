"""Settings."""

import os


class BaseConfig(object):
    """Base configuration."""

    DEBUG = False
    SECRET_KEY = "MY_VERY_SECRET_KEY"
    CSRF_ENABLED = True
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    DB_URI = ""
    PROPAGATE_EXCEPTIONS = True