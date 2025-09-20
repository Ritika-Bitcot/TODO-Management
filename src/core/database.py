# src/core/database.py
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.core.config import get_settings

# Setup logger
logger = logging.getLogger(__name__)

# Load current settings (development or testing)
settings = get_settings()

# Base class for all ORM models
Base = declarative_base()

from src.models.task_model import Task
from src.models.user_model import User

logger.debug(f"Loaded models: {User.__tablename__}, {Task.__tablename__}")

# Database engine
engine = create_engine(settings.sqlalchemy_database_uri, echo=True, future=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency-style helper (for services, repositories, tests)
def get_db():
    """
    Dependency-style helper for obtaining a database session.

    Yields:
        SessionLocal: A database session object.

    Notes:
        The session is automatically closed at the end of the generator block.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
