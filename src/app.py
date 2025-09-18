from flask import Flask

from config import Config
from routes.register import register_blueprints


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    register_blueprints(app)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
