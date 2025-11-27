
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


# Get the repository root directory (4 levels up from this file)
REPO_ROOT = Path(__file__).parent.parent.parent.parent.parent
ENV_FILE = REPO_ROOT / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE),
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'
    )

    # Database settings
    DATABASE_URL: str = "postgresql+asyncpg://fast-api:test1234@localhost:5432/fast-api"

    # Application settings
    debug: bool = False
    app_host: str = "0.0.0.0"
    app_port: int = 8000


@lru_cache(maxsize=1)  # Cache one instance; maxsize=1 enforces singleton
def get_settings() -> Settings:
    return Settings()
