# src/routes/auth_routes.py
from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.schemas.user_schema import UserLoginSchema, UserRegisterSchema
from src.services.auth_service import AuthService
from src.utils.exceptions import ServiceError
from src.utils.jwt_helper import JWTHelper

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register() -> tuple[dict, int]:
    """User registration endpoint with strong password validation."""
    try:
        user_data = UserRegisterSchema(**request.json)
        db: Session = next(get_db())
        user = AuthService.register_user(db, user_data.username, user_data.email, user_data.password)
        return (
            jsonify({"id": user.id, "username": user.username, "email": user.email}),
            201,
        )

    except ValidationError as e:
        errors = [{"loc": err["loc"], "msg": str(err["msg"])} for err in e.errors()]
        return jsonify({"errors": errors}), 400

    except ServiceError as e:
        return jsonify({"error": e.message}), getattr(e, "status_code", 400)

    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


@auth_bp.route("/login", methods=["POST"])
def login() -> tuple[dict, int]:
    """User login endpoint with JWT access & refresh tokens."""
    try:
        login_data = UserLoginSchema(**request.json)

        db: Session = next(get_db())
        user = AuthService.authenticate_user(db, login_data.email, login_data.password)
        if not user:
            return jsonify({"error": "Invalid credentials"}), 401

        access_token = JWTHelper.create_access_token({"user_id": user.id, "email": user.email})
        refresh_token = JWTHelper.create_refresh_token({"user_id": user.id, "email": user.email})

        return (
            jsonify({"access_token": access_token, "refresh_token": refresh_token}),
            200,
        )
    except ValidationError as e:
        errors = [{"loc": err["loc"], "msg": str(err["msg"])} for err in e.errors()]
        return jsonify({"errors": errors}), 400

    except ServiceError as e:
        return jsonify({"error": e.message}), getattr(e, "status_code", 400)

    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
