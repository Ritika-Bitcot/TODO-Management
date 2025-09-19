# src/utils/jwt_helper.py
from datetime import datetime, timedelta, timezone
from typing import Dict

import jwt

from src.constant import (
    JWT_ACCESS_TOKEN_EXPIRES,
    JWT_ALGORITHM,
    JWT_REFRESH_TOKEN_EXPIRES,
    JWT_SECRET_KEY,
)


class JWTHelper:
    """Helper class to create and decode JWT tokens."""

    @staticmethod
    def create_access_token(data: Dict[str, str], expires_delta: int = JWT_ACCESS_TOKEN_EXPIRES) -> str:
        """Generate a JWT access token."""
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    @staticmethod
    def create_refresh_token(data: Dict[str, str], expires_delta: int = JWT_REFRESH_TOKEN_EXPIRES) -> str:
        """Generate a JWT refresh token."""
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> Dict:
        """Decode a JWT token and return the payload."""
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
