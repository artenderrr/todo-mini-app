from typing import Annotated
import os
import json
import urllib.parse
from dotenv import load_dotenv
from fastapi import Header, HTTPException, Depends
from init_data import InitData
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