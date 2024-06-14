from aiogram import Dispatcher, Bot
from Config import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(config.TOKEN_BOT)
dp = Dispatcher(bot, storage = MemoryStorage())
