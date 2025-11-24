
from libs.shared.src.shared.database import engine



async def init_db():
    async with engine.begin() as conn:
        SQLModel.metadata.create_all(conn)