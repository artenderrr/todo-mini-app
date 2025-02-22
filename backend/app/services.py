from app.database import Session
from app.models import TaskModel

class TaskService:
    @staticmethod
    async def create_task(name: str, owner_id: int) -> None:
        async with Session() as session:
            task = TaskModel(name=name, owner_id=owner_id)
            session.add(task)
            await session.commit()