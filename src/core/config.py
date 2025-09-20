from datetime import timedelta

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    """Common settings loaded from environment or .env file."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Flask
    secret_key: str = Field(..., env="SECRET_KEY")

    # JWT
    jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")
    jwt_access_token_expires: int = Field(3600, env="JWT_ACCESS_TOKEN_EXPIRES")  # 1 hour in seconds
    jwt_refresh_token_expires: int = Field(86400, env="JWT_REFRESH_TOKEN_EXPIRES")  # 24 hours in seconds

    @field_validator("secret_key", "jwt_secret_key")
    def validate_non_empty(cls, v: str) -> str:
        """
        Validates that the given secret keys are not empty.

        Args:
            v (str): The secret key to be validated.

        Returns:
            str: The validated secret key.

        Raises:
            ValueError: If the secret key is empty.
        """
        if not v.strip():
            raise ValueError("Secret keys cannot be empty")
        return v

    @field_validator("jwt_access_token_expires", "jwt_refresh_token_expires")
    def validate_token_expiry(cls, v: int) -> int:
        """
        Validates that the given JWT expiry is positive.

        Args:
            v (int): The value to be validated.

        Returns:
            int: The validated value.

        Raises:
            ValueError: If the value is not positive.
        """
        if v <= 0:
            raise ValueError("JWT expiry must be positive")
        return v

    @property
    def jwt_access_expires_timedelta(self) -> timedelta:
        """
        A timedelta representing the time delta before the access token expires.

        This property is useful when creating tokens that expire after a certain time.
        It is calculated from the jwt_access_token_expires setting.

        :return: A timedelta object representing the time delta before the access token expires.
        :rtype: timedelta
        """
        return timedelta(seconds=self.jwt_access_token_expires)

    @property
    def jwt_refresh_expires_timedelta(self) -> timedelta:
        """
        A timedelta representing the time delta before the refresh token expires.

        This property is useful when creating tokens that expire after a certain time.
        It is calculated from the jwt_refresh_token_expires setting.

        :return: A timedelta object representing the time delta
        before the refresh token expires.
        :rtype: timedelta
        """
        return timedelta(seconds=self.jwt_refresh_token_expires)


class DevelopmentSettings(CommonSettings):
    """Development configuration with DB connection."""

    db_user: str = Field(..., env="DB_USER")
    db_password: str = Field(..., env="DB_PASSWORD")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")
    db_name: str = Field(..., env="DB_NAME")

    @field_validator("db_user", "db_password", "db_host", "db_name")
    def validate_non_empty_db_fields(cls, v: str) -> str:
        """
        Validates that the given database fields are not empty.

        Args:
            v (str): The value to be validated.

        Returns:
            str: The validated value.

        Raises:
            ValueError: If the value is empty.
        """

        if not v.strip():
            raise ValueError("Database fields cannot be empty")
        return v

    @field_validator("db_port")
    def validate_port(cls, v: int) -> int:
        """
        Validates that the given database port is between 1 and 65535.

        Args:
            v (int): The value to be validated.

        Returns:
            int: The validated value.

        Raises:
            ValueError: If the value is not between 1 and 65535.
        """
        if not (1 <= v <= 65535):
            raise ValueError("DB_PORT must be between 1 and 65535")
        return v

    @property
    def sqlalchemy_database_uri(self) -> str:
        """
        A URI string that can be used to connect to the database.

        This string is in the format expected by SQLAlchemy and includes the
        username, password, host, port, and database name.

        :return: A URI string that can be used to connect to the database.
        :rtype: str
        """
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}" f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


# Factory method
def get_settings(env: str = "development") -> CommonSettings:
    """
    Factory method to get the settings object based on the environment.

    Args:
        env (str, optional): The environment to use. Defaults to "development".

    Returns:
        CommonSettings: The settings object for the given environment.

    Raises:
        ValueError: If the environment is not supported.
    """
    env = env.strip().lower()
    if env == "development":
        return DevelopmentSettings()
    raise ValueError(f"Unsupported environment: {env}")
