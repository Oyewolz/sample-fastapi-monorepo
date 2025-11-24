

import os
from pydantic import BaseModel


class DBConfig(BaseModel):
     DATABASE_URL: str


def get_settings () -> DBConfig:
    return DBConfig(
        DATABASE_URL=os.getenv(
            "DATABASE_URL", "postgresql+asyncpg://fast-api:test1234@localhost:5432/fast-api")
    )