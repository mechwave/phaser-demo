"""Debug setting."""
import os
from app.tools.setting import BaseConfig


class ProdConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SWAGGER = {
        "swagger": "2.0",
        "info": {
            "title": "API",
            "description": "Application programming interface.",
            "version": "1.0.0"
        },
        "schemes": [
            "http"
        ]
    }