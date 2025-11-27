from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from fastapi import FastAPI
from shared_lib.database import engine
# Import models so SQLModel knows about them
from shared_lib.database.models import FTUser, Role
from .config import get_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="User Service", lifespan=lifespan,
              debug=get_config().debug
              )
