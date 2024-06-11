from aiogram.types import BotCommand
from LoadInterface import strings


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Запуск бота"),
        BotCommand(command="/register", description=strings["SignUp"]),
        BotCommand(command="/enter_scores", description=strings["RecordScore"]),
        BotCommand(command="//view_scores", description=strings["CheckScore"])
    ]
    await bot.set_my_commands(commands)
