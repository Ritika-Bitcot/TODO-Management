import os

from flask import Flask

from config import get_settings
from routes.register import register_blueprints


def create_app(env: str | None = None) -> Flask:
    """
    Create and configure the Flask application.

    Args:
        env (str | None): Environment ("development" or "testing").

    Returns:
        Flask: The Flask application instance.
    """
    env = env or os.getenv("FLASK_ENV", "development")
    settings = get_settings(env)

    app = Flask(__name__)

    # Apply config from settings
    app.config["SECRET_KEY"] = settings.secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.sqlalchemy_database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = settings.jwt_secret_key
    app.config["JWT_ALGORITHM"] = settings.jwt_algorithm
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = settings.jwt_access_expires_timedelta
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = settings.jwt_refresh_expires_timedelta

    register_blueprints(app)
    return app


app = create_app(env=os.getenv("FLASK_ENV", "development"))


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
