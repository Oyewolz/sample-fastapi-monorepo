"""Test script to verify database table creation"""
import asyncio
from sqlmodel import SQLModel
from shared_lib.database import engine
from shared_lib.models import FTUser, Role


async def create_tables():
    """Create all tables in the database"""
    print("Creating tables...")
    print(f"Models registered: {SQLModel.metadata.tables.keys()}")
    
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    
    print("Tables created successfully!")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(create_tables())

