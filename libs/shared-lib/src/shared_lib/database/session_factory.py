from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from .engine import engine

AsyncSessionLocal = sessionmaker( engine, class_=AsyncSession, expire_on_commit=False )
