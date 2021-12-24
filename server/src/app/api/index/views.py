"""Views."""

from flask import Blueprint, render_template, Response, current_app


index_blueprint = Blueprint(
    'index', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/',
)


@index_blueprint.route('/')
def get_index():
    """Get index."""
    return render_template('index.html',)
