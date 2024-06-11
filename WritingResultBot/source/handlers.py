from aiogram import Dispatcher

from dispatcher import dp, bot

def register_handlers():
    @dp.message_handler()
    async def hello(message):
        await bot.send_message(message.chat.id, message.text)



