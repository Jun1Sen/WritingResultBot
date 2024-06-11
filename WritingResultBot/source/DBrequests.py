from DB import engine, async_session_fabric
from models import Base


requests = {


}

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def insert_data(objDB: []):
    async with async_session_fabric() as session:
        session.add_all(objDB)
        await session.commit()



