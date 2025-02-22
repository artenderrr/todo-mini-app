from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str

class TaskSchema(BaseModel):
    name: str = Field(min_length=1, max_length=20)