from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from fastapi import FastAPI
from app.models import create_database_tables


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await create_database_tables()
    yield

app = FastAPI(lifespan=lifespan)