from misc import bot, dp, conn, cursor
from aiogram import types
import handlers.keyboard as kb
from config import admin
from .function import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from .ddos import *
from .st import *
import time

req = r.get("https://api.proxyscrape.com/?request=displayproxies")
array = req.text.split()

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    discription = "Привет👋"
    photo = open('media/hello.jpeg', 'rb')
    user = new_user(message.chat.id)
    if message.chat.id == admin:
        await bot.send_photo(message.chat.id,photo,discription , reply_markup=kb.main)
        await bot.send_message(message.chat.id,'Навигация в боте доступна по кнопкам ниже')
    if user == 'new user':
        await bot.send_photo(message.chat.id, photo, discription, reply_markup=kb.main)
        await bot.send_message(message.chat.id, 'У вас есть реферальный код?Если есть напишите /ref код')

@dp.message_handler(content_types=['text'], text='Профиль')
async def handfler(message: types.Message):
    photo = open('media/profile.jpeg', 'rb')
    if message.chat.id == admin:
        check = check_sub(message.chat.id)
        if not check:
            await bot.send_photo(message.chat.id,photo,f'Ваш ID:{message.chat.id}👾\nПодписка:не активна😞',
                                   reply_markup=kb.adm)
        elif check:
            await bot.send_photo(message.chat.id,photo, f'Ваш ID:{message.chat.id}👾\nПодписка:активна👑',
                                  reply_markup=kb.adm)
    else:
        check = check_sub(message.chat.id)
        if not check:
            await bot.send_photo(message.chat.id,photo, f'Ваш ID:{message.chat.id}👾\nПодписка:не активна😞',
                                   reply_markup=kb.menu)
        elif check:
            await bot.send_photo(message.chat.id,photo, f'Ваш ID:{message.chat.id}👾\nПодписка:активна👑',
                                   reply_markup=kb.menu)

@dp.message_handler(text=['Реферальная система'])
async def referal_system(message: types.Message):
    photo = open('media/ref.jpg', 'rb')
    balance = get_balance(message.chat.id)
    await bot.send_photo(message.chat.id, photo , f'Получите 10% от пополнения ваших рефералов💳\nБаланс от рефералов:{balance}₽\nВаш реферальный код:{message.chat.id}⚙️\nКоличество ваших рефералов:{get_referals(message.chat.id,message.chat.id)}⭐️')

@dp.message_handler(text=['Назад'])
async def referal_system(message: types.Message):
	photo = open('media/menu.jpg', 'rb')
	await bot.send_photo(message.chat.id,photo,"Главное меню",reply_markup=kb.main)
	
@dp.message_handler(text=['Инфо'])
async def referal_system(message: types.Message):
	photo = open('media/info.jpg', 'rb')
	desc = "Бот является собственностью  хуй знает кого, админ не знает про бота, мы не несём ответственности за ваши действия .. по всем вопросам @uuiuuka"
	await bot.send_photo(message.chat.id,photo,desc,reply_markup=kb.main)
	
@dp.message_handler(content_types=['text'], text='DDoS')
async def ddos(message: types.Message):
    check = check_sub(message.chat.id)
    if not check or check == None:
    	await bot.send_message(message.chat.id, 'У вас нет подписки!Для покупки напишете Оплата')
    else:
    		await bot.send_message(message.chat.id,"Отправтье сайт или ip адрес для DDoSa,для отмены нажмите кнопку ниже",reply_markup=kb.back)
    		await st.url.set()
    		await state.finish()
      	
      		
      			
@dp.message_handler(state=st.url)

async def proc(message: types.Message, state: FSMContext):
	   		if message.text == '⏪ Назад':
	   			await bot.send_message(message.chat.id,"Отмена,возвращаю назад!",reply_markup=kb.main)
	   		else:
	   			await bot.send_message(message.chat.id,"Запускаю DDoS на {}".format(message.text))
	   			await bot.send_message(message.chat.id,"DDoS будет автоматически остановлен через 5 минут!"    ,reply_markup=kb.main)
	   			await state.finish()	 	
	   			await check_prox(array,st)