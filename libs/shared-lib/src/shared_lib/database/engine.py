
from sqlalchemy.ext.asyncio import create_async_engine
from .db_config import get_db_config

db_config = get_db_config()
engine = create_async_engine(db_config.DATABASE_URL,
                              echo=True,
                              future=True,
                              pool_size=10,
                              max_overflow=20
                            )
