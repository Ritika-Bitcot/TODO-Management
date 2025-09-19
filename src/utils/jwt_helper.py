from datetime import datetime, timezone
from typing import Dict

import jwt

from src.core.config import get_settings

# Load settings based on environment
settings = get_settings()


class JWTHelper:
    """Helper class to create and decode JWT tokens."""

    @staticmethod
    def create_access_token(data: Dict[str, str]) -> str:
        """Generate a JWT access token."""
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + settings.jwt_access_expires_timedelta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

    @staticmethod
    def create_refresh_token(data: Dict[str, str]) -> str:
        """Generate a JWT refresh token."""
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + settings.jwt_refresh_expires_timedelta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

    @staticmethod
    def decode_token(token: str) -> Dict:
        """Decode a JWT token and return the payload."""
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
