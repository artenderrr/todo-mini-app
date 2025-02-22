from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from fastapi import FastAPI, APIRouter
from app.models import create_database_tables
from app.schemas import BaseTaskSchema, TaskSchema, TaskUpdateFieldsSchema
from app.services import TaskService
from app.dependencies import CurrentUser, TaskOwnedByCurrentUser


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await create_database_tables()
    yield

app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix="/api")


@router.get("/tasks")
async def get_tasks(user: CurrentUser) -> list[TaskSchema]:
    tasks = await TaskService.get_tasks_by_owner(owner_id=user.id)
    return tasks

@router.post("/tasks", status_code=201)
async def create_task(task: BaseTaskSchema, user: CurrentUser) -> BaseTaskSchema:
    await TaskService.create_task(
        name=task.name,
        owner_id=user.id
    )
    return task

@router.put("/tasks/{task_id}")
async def update_task(
    task_id: TaskOwnedByCurrentUser,
    update_fields: TaskUpdateFieldsSchema
) -> TaskSchema:
    updated_task = await TaskService.update_task(task_id, update_fields)
    return updated_task

@router.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: TaskOwnedByCurrentUser) -> None:
    await TaskService.delete_task(task_id)


app.include_router(router)