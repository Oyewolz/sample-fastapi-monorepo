

from pydantic import BaseModel
from shared_lib.config.setting import get_settings

class DBConfig(BaseModel):
     DATABASE_URL: str


def get_db_config() -> DBConfig:
    return DBConfig(
        DATABASE_URL=get_settings().DATABASE_URL
    )