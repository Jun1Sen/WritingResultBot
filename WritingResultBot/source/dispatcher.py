from aiogram import Dispatcher, Bot
from Config import config

bot = Bot(config.TOKEN_BOT)
dp = Dispatcher(bot)
