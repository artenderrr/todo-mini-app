from typing import Annotated
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from fastapi import FastAPI, APIRouter, Depends
from app.models import create_database_tables
from app.schemas import TaskSchema, UserSchema
from app.services import TaskService
from app.dependencies import current_user


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await create_database_tables()
    yield

app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix="/api")


@router.post("/tasks", status_code=201)
async def create_task(
    task: TaskSchema,
    user: Annotated[UserSchema, Depends(current_user)]
) -> TaskSchema:
    await TaskService.create_task(
        name=task.name,
        owner_id=user.id
    )
    return task


app.include_router(router)