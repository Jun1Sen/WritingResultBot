from LoadInterface import strings
from dispatcher import dp, bot

def register_handlers():
    @dp.message_handler(commands='/start')
    async def hello(message):
        await bot.send_message(message.chat.id, strings["Hello"])

    @dp.message_handler(commands='/register')
    async def register(message):
        pass

    @dp.message_handler(commands='/enter_scores')
    async def enter_scores(message):
        pass

    @dp.message_handler(commands='/view_scores')
    async def view_scores(message):
        pass



