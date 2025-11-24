from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield
    print("Shutting down")


app = FastAPI(title="User Service")
