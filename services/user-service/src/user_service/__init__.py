from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from fastapi import FastAPI
from shared_lib.database import engine
# Import models so SQLModel knows about them
from shared_lib.database.models import FTUser, Role
from .config import get_config
from .routes.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="User Service", lifespan=lifespan,
              debug=get_config().debug
              )

app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Hello from user-service!"}


@app.on_event("startup")
async def startup_event():
    print("Starting user-service...")
