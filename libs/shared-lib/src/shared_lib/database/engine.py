
from sqlalchemy.ext.asyncio import create_async_engine
from .db_config import get_settings

settings = get_settings()
engine = create_async_engine(settings.DATABASE_URL, 
                              echo=True,
                              future=True,
                              pool_size=10,
                              max_overflow=20
                            )
