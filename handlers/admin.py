from misc import bot, dp, conn, cursor
from aiogram import types
import handlers.keyboard as kb
from config import admin
from .function import *


@dp.message_handler(content_types=['text'], text='Админ панель')
async def handfler(message: types.Message):
    photo = open('media/admin.jpeg', 'rb')
    if message.chat.id == admin:
        await bot.send_photo(message.chat.id, photo,'Вы вошли в админ панель.\n/sub @ТЕЛЕГРАММ ID - выдать бесплатную подписку\n/changebalance @ТЕЛЕГРАММ ID - сбросить реферальный баланс до нуля')
    else:
        await bot.send_message(message.chat.id, 'У вас нет доступа к админ панели!')
                               
@dp.message_handler(content_types=['text'])
async def admin_commands(message: types.Message):
    if '/sub' in message.text:
        chat_id = message.chat.id
        telegram_id = message.text.replace('/sub', '').replace(' ', '')
        if chat_id == 1270842436:
            new_user(telegram_id)
            add_sub(telegram_id)
            await bot.send_message(message.chat.id, 'Выдал бесплатный доступ👥')
            try:
                await bot.send_message(telegram_id, 'Вам выдали бесплатный доступ к боту🤩')
            except:
                pass
        else:
            await bot.send_message(message.chat.id, 'У вас нет доступа к данной функции!')
    elif '/ref' in message.text:
        promo = message.text.replace('/ref', ' ').replace(' ', '')
        add_promo(message.chat.id, promo)
        await bot.send_message(message.chat.id, 'Промокод активирован!')                                            