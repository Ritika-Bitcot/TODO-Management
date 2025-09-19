from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.models.user_model import User
from src.utils.exceptions import ServiceError
from src.utils.password_helper import PasswordHelper


class AuthService:
    """Service layer for handling user authentication and registration."""

    @staticmethod
    def register_user(db: Session, username: str, email: str, password: str) -> User:
        """
        Register a new user with hashed password.

        Raises:
            ServiceError: If database commit fails.
        """
        try:
            hashed_password = PasswordHelper.hash_password(password)
            user = User(username=username, email=email, password_hash=hashed_password)
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except SQLAlchemyError as e:
            db.rollback()
            raise ServiceError("Database error during user registration") from e
        except Exception as e:
            raise ServiceError(f"Unexpected error during registration: {str(e)}")

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        """
        Authenticate a user by verifying credentials.

        Raises:
            ServiceError: If unexpected error occurs.
        """
        try:
            user = db.query(User).filter(User.email == email).first()
            if user and PasswordHelper.verify_password(password, user.password_hash):
                return user
            return None
        except Exception as e:
            raise ServiceError(f"Unexpected error during authentication: {str(e)}")
