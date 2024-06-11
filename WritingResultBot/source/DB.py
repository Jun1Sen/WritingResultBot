from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, DeclarativeBase
from typing import Annotated
from sqlalchemy import URL, create_engine, String, BigInteger, SmallInteger
from Config import config
from asyncio import run

engine = create_async_engine(
    url = config.DB_URL_asyncpg(),
    echo = False
)

async_session_fabric = async_sessionmaker(bind=engine)

str_50 = Annotated[str, 50]
bigint = Annotated[BigInteger, 123456789876543234567876543456]

class Base(DeclarativeBase):
    type_annotation_map ={
        str_50: String(50)
    }
    pass


