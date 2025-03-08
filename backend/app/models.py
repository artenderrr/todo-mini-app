from sqlalchemy import Identity, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, engine


class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    done: Mapped[bool] = mapped_column(default=False)
    owner_id: Mapped[int] = mapped_column(BigInteger)


async def create_database_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)