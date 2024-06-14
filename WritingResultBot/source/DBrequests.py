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


async def get_user_id(telegramID: int) -> int:
    async with async_session_fabric() as session:
        query = (
            select(User).select_from(User).filter(User.telegramId == telegramID)
        )
        res = await session.execute(query)
        result = res.scalars().first().__dict__.get('id')
        print(result)
        if result is None: return -1
        return result


async def select_score_by_ID(telegramID: int) -> [dict]:
    async with async_session_fabric() as session:
        query = (
            select(ResultEGE, User)
            .join(ResultEGE, User.id == ResultEGE.user_id)
            .filter(User.telegramId == telegramID)
        )
        print(query)
        res = await session.execute(query)
        objects = list(res.scalars().all())
        results = []
        for x in objects:
            subject = x.__dict__.get('subject')
            score = x.__dict__.get('result')
            results.append({"subject": subject, "score": score})
        return results


async def insert_score(telegramID: int, subject: str, score: int) -> bool:
    userId = await get_user_id(telegramID)
    score = ResultEGE(user_id=userId, subject=subject, result=score)
    async with async_session_fabric() as session:
        session.add_all([score])
        await session.commit()


async def insert_user(telegramId: int, FirstName: str, SecondName: str | None):
    user = User(telegramId=telegramId, FirstName=FirstName, SecondName=SecondName)
    async with async_session_fabric() as session:
        session.add_all([user])
        await session.commit()
