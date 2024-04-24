import telebot
from telebot import types

TOKEN = ''

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    about = types.InlineKeyboardButton('About Us', callback_data='company_info_message')
    work = types.InlineKeyboardButton('Work Positions', callback_data='show_work_positions')
    contacts = types.InlineKeyboardButton('Contacts', callback_data='show_contacts')
    req_and_con = types.InlineKeyboardButton('Requirements and Conditions', callback_data='show_requirements_and_conditions')

    markup.add(about, work, contacts, req_and_con)
    
    bot.send_message(message.chat.id, 'Welcome to Queen Bee! \nUse buttons to explore more.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def fork(callback):
    if callback.message:
        if callback.data == 'company_info_message':
            bot.send_message(callback.message.chat.id, "🐝 Queen Bee Poland is the world’s leading B2B provider of innovative iGaming Studio products. \nWe offer opportunities for growth. Join and start you career. 🐝")
        elif callback.data == 'show_contacts':
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            hr = types.InlineKeyboardButton(text='HR Department', url='https://t.me/hrqueenbee')
            recr = types.InlineKeyboardButton(text='Recruitment', url='https://t.me/dariarecruitmentt')
            keyboard.add(hr,recr)
            bot.send_message(callback.message.chat.id, 'We will answer you as soon as possible.', reply_markup=keyboard)
        elif callback.data == 'show_requirements_and_conditions':
            bot.send_message(callback.message.chat.id, 'Requirements and Conditions.........bla bla bla')
        
        
        elif callback.data == 'show_work_positions':
            markup = types.InlineKeyboardMarkup(row_width=1)
            sm = types.InlineKeyboardButton('Service Manager (for males only)', callback_data='service_manager')
            gp = types.InlineKeyboardButton('Game Presenter (for females only)', callback_data='game_presenter')

            markup.add(sm, gp)
            bot.send_message(callback.message.chat.id, 'Available work positions.', reply_markup=markup)
        elif callback.data == 'service_manager':
            markup = types.InlineKeyboardMarkup(row_width=1)
            sm = types.InlineKeyboardButton('Good EnG', callback_data='good_eng_cv')
            gp = types.InlineKeyboardButton('Bad Eng', callback_data='bad_eng_cv')

            markup.add(sm, gp)
            bot.send_message(callback.message.chat.id, 'Your Eng is ...', reply_markup=markup)
        elif callback.data == 'good_eng_cv':
            bot.send_message(callback.message.chat.id, 'Now send your CV, please.')
            
            

    
    


bot.infinity_polling()