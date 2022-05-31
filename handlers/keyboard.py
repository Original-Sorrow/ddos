from aiogram import types



menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton('Оплата'),
    types.KeyboardButton('Реферальная система'),
    types.KeyboardButton('DDoS')
)
menu.add('Назад')

adm = types.ReplyKeyboardMarkup(resize_keyboard=True)
adm.add(
    types.KeyboardButton('Оплата'),
    types.KeyboardButton('Реферальная система'),
    types.KeyboardButton('DDoS'))
adm.add(types.KeyboardButton('Админ панель'))
adm.add('Назад')

main = types.ReplyKeyboardMarkup(resize_keyboard=True)
main.add(types.KeyboardButton('Профиль'))
main.add('Инфо')


stop = types.ReplyKeyboardMarkup(resize_keyboard=True)
stop.add(types.KeyboardButton('Стоп'))

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('Назад'))                        