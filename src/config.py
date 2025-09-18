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
    TEST_DB_HOST,
    TEST_DB_NAME,
    TEST_DB_PASSWORD,
    TEST_DB_PORT,
    TEST_DB_USER,
)


class Config:
    """Base configuration loaded from constants/env."""

    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY = JWT_SECRET_KEY
    JWT_ALGORITHM = JWT_ALGORITHM
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=JWT_ACCESS_TOKEN_EXPIRES)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=JWT_REFRESH_TOKEN_EXPIRES)


class DevelopmentConfig(Config):
    """Configuration for development environment."""

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    DEBUG = True


class TestingConfig(Config):
    """Configuration for testing environment."""

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{TEST_DB_USER}:{TEST_DB_PASSWORD}" f"@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"
    )
    TESTING = True
    DEBUG = False
