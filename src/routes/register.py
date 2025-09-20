from flask import Flask

from .auth_routes import auth_bp
from .home_routes import home_bp


def register_blueprints(app: Flask) -> None:
    """
    Register all application blueprints with the Flask app.

    Args:
        app (Flask): The Flask application instance.
    """
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
