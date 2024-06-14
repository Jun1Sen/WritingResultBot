from DBrequests import create_tables, drop_tables, insert_user, select_score_by_ID, insert_score, check_existing_user
from handlers import dp, register_handlers, bot
from commands import set_commands
from models import User
from asyncio import get_event_loop
from aiogram import executor



async def setup():
    await drop_tables()
    await create_tables()
    await insert_user(telegramId=3434343, FirstName="John", SecondName="Sina")
    print(await check_existing_user(3434343))
    await insert_score(3434343, "English", 87)
    await insert_score(3434343, "English", 87)
    print(await select_score_by_ID(3434343))

    # register_handlers()
    # await set_commands(bot)


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(setup())
    # executor.start_polling(dp, skip_updates=True)
