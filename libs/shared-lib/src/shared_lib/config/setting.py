
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str


@lru_cache(maxsize=1)  # Cache one instance; maxsize=1 enforces singleton
def get_settings() -> Settings:
    return Settings()
