from aiogram import executor, types
from misc import dp, bot
import handlers
from LiteSQL import lsql
from aiogram.types import ContentType
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent, ParseMode
					
	
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
