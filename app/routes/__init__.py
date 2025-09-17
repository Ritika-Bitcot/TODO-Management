from flask import Flask
from .home_routes import home_bp

def register_blueprints(app: Flask) -> None:
    """
    Register all application blueprints with the Flask app.

    Args:
        app (Flask): The Flask application instance.
    """
    app.register_blueprint(home_bp)
