import os
from typing import cast
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


load_dotenv()

engine = create_async_engine(cast(str, os.getenv("DB_URL")))
Session = async_sessionmaker(engine)


class Base(DeclarativeBase):
	pass