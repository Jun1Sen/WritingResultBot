from DBrequests import create_tables, insert_data, drop_tables
from dispatcher import dp

from asyncio import run
from aiogram import executor


async def main():
    await drop_tables()
    await create_tables()
    await insert_data()




if __name__ == '__main__':
    run(main())
    executor.start_polling(dp, skip_updates=True)

