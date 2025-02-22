from sqlalchemy import select
from app.database import Session
from app.models import TaskModel
from app.schemas import TaskSchema, TaskUpdateFieldsSchema

class TaskService:
    @staticmethod
    async def get_tasks_by_owner(*, owner_id: int) -> list[TaskSchema]:
        async with Session() as session:
            models = (await session.execute(
                select(TaskModel).where(TaskModel.owner_id == owner_id)
            )).scalars()
            tasks = [TaskSchema(**model.__dict__) for model in models]
            return tasks

    @staticmethod
    async def create_task(*, name: str, owner_id: int) -> None:
        async with Session() as session:
            task = TaskModel(name=name, owner_id=owner_id)
            session.add(task)
            await session.commit()

    @staticmethod
    async def update_task(task_id: int, update_fields: TaskUpdateFieldsSchema) -> TaskSchema:
        async with Session() as session:
            task = await session.get(TaskModel, task_id)
            for field, value in update_fields.model_dump(exclude_defaults=True).items():
                setattr(task, field, value)
            updated_task = TaskSchema(**task.__dict__)
            await session.commit()
        return updated_task

    @staticmethod
    async def delete_task(task_id: int) -> None:
        async with Session() as session:
            task = await session.get(TaskModel, task_id)
            await session.delete(task)
            await session.commit()