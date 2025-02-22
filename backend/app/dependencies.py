from typing import Annotated
import os
import json
import urllib.parse
from dotenv import load_dotenv
from fastapi import Header, HTTPException, Depends
from init_data import InitData
from app.database import Session
from app.models import TaskModel
from app.schemas import UserSchema


load_dotenv()


def _decode_init_data(init_data: str, *, times_to_decode: int = 1) -> str:
    for i in range(times_to_decode):
        init_data = urllib.parse.unquote(init_data)
    return init_data

def _parse_init_data(init_data: str) -> dict[str, str]:
    result = {}
    for entry in init_data.split("&"):
        key, value = entry.split("=")
        result[key] = value
    return result


def valid_init_data(authorization: Annotated[str, Header()]) -> str:
    if (
        not authorization.startswith("tma ")
        or
        not InitData(authorization[4:], os.getenv("BOT_TOKEN")).validate(times_to_decode=2) # type: ignore
    ):
        raise HTTPException(status_code=401, detail="Invalid initialization data")
    return authorization[4:]

def current_user(init_data: Annotated[str, Depends(valid_init_data)]) -> UserSchema:
    decoded_init_data = _decode_init_data(init_data, times_to_decode=2)
    init_data_dict = _parse_init_data(decoded_init_data)
    current_user_data = json.loads(init_data_dict["user"])
    return UserSchema(**current_user_data)


CurrentUser = Annotated[UserSchema, Depends(current_user)]


async def task_owned_by_current_user(
    task_id: int,
    user: CurrentUser
) -> int:
    async with Session() as session:
        model = await session.get(TaskModel, task_id)
        if not model:
            raise HTTPException(status_code=404, detail="Task with provided ID doesn't exist")
        if model.owner_id != user.id:
            raise HTTPException(status_code=403, detail="Task with provided ID belongs to another user")
    return task_id