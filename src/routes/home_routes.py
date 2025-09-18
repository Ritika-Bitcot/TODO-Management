from flask import Blueprint, jsonify

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home() -> tuple[dict, int]:
    """
    Home endpoint that returns a simple Hello World message.

    Returns:
        tuple[dict, int]: A JSON response with a message and HTTP status code.
    """
    return jsonify({"message": "Welcome to Todo Management Application!"}), 200
