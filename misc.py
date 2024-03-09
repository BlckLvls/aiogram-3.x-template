import logging
from aiogram import Bot, Dispatcher, types
from handlers import start
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os


load_dotenv()

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=os.environ.get('BOT_TOKEN'))
# Диспетчер
dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(start.router)