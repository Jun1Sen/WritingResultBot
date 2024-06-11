from DB import engine, async_session_fabric
from models import Base, User, ResultEGE

from sqlalchemy import select


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def check_existing_user(telegramID: int) -> bool:

    async with async_session_fabric() as session:
        query = (
            select(User.telegramId).select_from(User).filter(User.telegramId == telegramID)
        )
        res = await session.execute(query)
        result = res.scalars().first()
        if result is None: return False
        return True


async def select_score_by_ID(telegramID: int) -> ResultEGE:
    async with async_session_fabric() as session:
        query = (
            select(User, ResultEGE)
            .join(ResultEGE, User.id == ResultEGE.user_id)
            .filter(User.telegramId == telegramID)
        )
        result = await session.execute(query)
        user_profile = result.first()
        return user_profile

async def insert_score(telegramID: int, subject: str, score: int) -> bool:
    score = ResultEGE(user_id = telegramID, subject = subject, result = score)
    async with async_session_fabric() as session:
        session.add_all([score])
        await session.commit()


async def insert_user(telegramId: int, FirstName: str, SecondName: str | None):
    user = User(telegramId=telegramId, FirstName=FirstName, SecondName=SecondName)
    async with async_session_fabric() as session:
        session.add_all([user])
        await session.commit()
