import os

from flask import Flask

from config import DevelopmentConfig, TestingConfig
from routes.register import register_blueprints


def create_app(env: str = "development") -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__)
    if env == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    register_blueprints(app)
    return app


app = create_app(env=os.getenv("FLASK_ENV", "development"))


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
