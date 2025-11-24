
from shared_lib.config.setting import Settings
from functools import lru_cache as LRU_cache

class Config(Settings):
    pass


@LRU_cache(maxsize=1)  # Cache one instance; maxsize=1 enforces singleton
def get_config() -> Config:
    return Config() 