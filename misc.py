import asyncio, sqlite3, pytz
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage(), loop=loop)
conn = sqlite3.connect("BD/bomber_users.db")
cursor = conn.cursor()

