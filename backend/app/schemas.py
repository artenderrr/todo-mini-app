from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: int
    username: str | None = None
    first_name: str
    last_name: str

class BaseTaskSchema(BaseModel):
    name: str = Field(min_length=1, max_length=64)

class TaskSchema(BaseTaskSchema):
    id: int
    done: bool
    owner_id: int

class TaskUpdateFieldsSchema(BaseModel):
    name: str | None = Field(min_length=1, max_length=64, default=None)
    done: bool | None = None