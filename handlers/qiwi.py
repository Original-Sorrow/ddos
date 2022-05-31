from misc import bot, dp, conn, cursor
from .function import *
import requests
from multiprocessing import Process, Queue
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.helper import Helper, HelperMode, ListItem
import os
import json
import random



phone ="+79379399720"
token ="6edf82"
amount = 10
publick_key = "48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPyYkRWf2pMNoP1yPYby4gdfRcLsY5FLu7Nq8rrF9FrXxBWUdNKBdcDPk75UfsLZXWn67uAMf1DPo6GPK2HFyAvsXQZZVusXgSrss6kVk4c"
photo = open('media/oplata.jpeg', 'rb')

@dp.message_handler(text=['Оплата'])
async def payment(message: types.Message):
    check = check_sub(message.chat.id)
    if not check:
        comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
        s = requests.Session()
        s.headers['authorization'] = 'Bearer' + token
        parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
        h = s.get('https://oplata.qiwi.com/create', params = parameters)
        inlinepay_keyboard = types.InlineKeyboardMarkup()
        pay_sub = types.InlineKeyboardButton('Оплатить подписку(qiwi)', url=h.url)
        pay_adm = types.InlineKeyboardButton('Оплатить подписку через админа(любой способ)', url="https://t.me/uuiuuka")
        check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay')
        pay_sub_balance = types.InlineKeyboardButton(text='Оплатить с баланса в боте',callback_data='checkbalance')
        inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(pay_sub_balance).add(check_pay).add(pay_adm)
        await bot.send_message(message.chat.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
        new_payment(message.chat.id,comment,amount)
    elif check:
        await bot.send_message(message.chat.id, 'Вы уже купили подписку,удачного пользования!', reply_markup=main_keyboard)
    


@dp.callback_query_handler(text='checkpay')
async def check_payment(query: types.CallbackQuery):
    comment = get_comment(query.message.chat.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                await bot.send_photo(query.message.chat.id,photo,'Оплата прошла,добавил вас в базу')
                inviter = referal_pay(query.message.chat.id)
                await bot.send_message(inviter, 'Ваш реферал оплатил подписку вам начислено 10%🤑')
                add_sub(query.message.chat.id)
                break
        else:
            await bot.send_message(query.message.chat.id, 'Не нашел вашу оплату')
            break

@dp.callback_query_handler(text='checkbalance')
async def check_balance(query: types.CallbackQuery):
    pay = checkbalance(query.message.chat.id)
    if pay:
        await bot.send_message(query.message.chat.id, 'Вы успешно купили подписку💎')
    elif not pay:
        await bot.send_message(query.message.chat.id, 'На вашем балансе не достаточно денег!')
