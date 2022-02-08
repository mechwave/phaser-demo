"""App."""

from flask import Flask, send_from_directory


def internal_server_error(e):
    print(e)
    return 'oops', 500


def get_app(config) -> Flask:
    """Get flask application."""
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/<path:path>')
    def send_path(path):
        return send_from_directory('templates/', path)

    from flask_marshmallow import Marshmallow
    Marshmallow(app)

    from flasgger import Swagger
    Swagger(app)

    from .api import blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint.obj, url_prefix = blueprint.url_prefix)

    #app.register_error_handler(Exception, internal_server_error)


    from sqlalchemy import create_engine
    from .models.map import Base
    Base.metadata.create_all(create_engine(app.config.get('SQLALCHEMY_DATABASE_URI', '')))

    return app
