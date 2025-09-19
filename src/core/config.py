from datetime import timedelta

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    """Common settings loaded from environment or .env file."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Flask
    secret_key: str = Field(..., env="SECRET_KEY")

    # JWT
    jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")
    jwt_access_token_expires: int = Field(3600, env="JWT_ACCESS_TOKEN_EXPIRES")  # seconds
    jwt_refresh_token_expires: int = Field(3600, env="JWT_REFRESH_TOKEN_EXPIRES")  # seconds

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


class TestingSettings(CommonSettings):
    """Testing configuration (should be used only in CI/CD or test runners)."""

    test_db_user: str = Field(..., env="TEST_DB_USER")
    test_db_password: str = Field(..., env="TEST_DB_PASSWORD")
    test_db_host: str = Field(..., env="TEST_DB_HOST")
    test_db_port: int = Field(..., env="TEST_DB_PORT")
    test_db_name: str = Field(..., env="TEST_DB_NAME")

    @property
    def sqlalchemy_database_uri(self) -> str:
        return (
            f"postgresql+psycopg2://{self.test_db_user}:{self.test_db_password}"
            f"@{self.test_db_host}:{self.test_db_port}/{self.test_db_name}"
        )


# Factory method to get settings dynamically
def get_settings(env: str = "development") -> CommonSettings:
    """
    Factory method to get settings dynamically.

    This method takes an environment string as an argument and
    returns the corresponding settings object.

    :param env: The environment string. Can be either "development" or "testing".
    :type env: str
    :return: The settings object for the given environment.
    :rtype: CommonSettings
    """
    if env == "testing":
        return TestingSettings()
    return DevelopmentSettings()
