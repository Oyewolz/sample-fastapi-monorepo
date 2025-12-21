
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

""" Rely on docker to pick up env variables """
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'
    )

    # Database settings
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    # Application settings
    debug: bool = False
    app_host: str = "0.0.0.0"
    app_port: int = 8000


@lru_cache(maxsize=1)  # Cache one instance; maxsize=1 enforces singleton
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
