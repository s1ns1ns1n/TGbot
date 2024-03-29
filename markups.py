from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

#type_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#type_markup_btn1 = types.KeyboardButton('Sports')
#type_markup_btn2 = types.KeyboardButton('E-sports')
#type_markup.add(type_markup_btn1, type_markup_btn2)

source_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Результаты')
source_markup_btn2 = types.KeyboardButton('Ближайшие матчи')
source_markup_btn3 = types.KeyboardButton('Топ-5 команд')
source_markup.add(source_markup_btn1, source_markup_btn2, source_markup_btn3)

back_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
back_markup_btn1 = types.KeyboardButton('/Назад')
back_markup.add(back_markup_btn1)