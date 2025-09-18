# src/config.py
from datetime import timedelta

from constant import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
    JWT_ACCESS_TOKEN_EXPIRES,
    JWT_ALGORITHM,
    JWT_REFRESH_TOKEN_EXPIRES,
    JWT_SECRET_KEY,
    SECRET_KEY,
)


class Config:
    """Base configuration loaded from constants/env."""

    SECRET_KEY = SECRET_KEY

    # Build database URL dynamically
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY = JWT_SECRET_KEY
    JWT_ALGORITHM = JWT_ALGORITHM
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=JWT_ACCESS_TOKEN_EXPIRES)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=JWT_REFRESH_TOKEN_EXPIRES)
