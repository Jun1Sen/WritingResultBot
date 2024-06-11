from DBrequests import create_tables, insert_data, drop_tables
from handlers import dp, register_handlers
from models import User
from asyncio import run, get_event_loop
from aiogram import executor


# async def main():
#     await drop_tables()
#     await create_tables()
#     # await insert_data()
#     register_handlers()
#     await executor.start_polling(dp, skip_updates=True)
#
#
#
# if __name__ == '__main__':
#     run(main())


async def setup():
    register_handlers()
    await drop_tables()
    await create_tables()
    await insert_data([User(telegramId=3434343, FirstName="John", SecondName="Sina")])





if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(setup())
    executor.start_polling(dp, skip_updates=True)
