#добавить эмодзи 
#ПЕРЕДЕЛАТЬ ЗАЯВКИ
import telebot
from telebot import types
import time
from threading import Thread
global user

#from db import BotDB
#BotDB = BotDB('application.db')

TOKEN = "5826775960:AAEWf_U8dZ1grUnEDeYZp1emPE3Rr8Ya_cc"

bot = telebot.TeleBot('5826775960:AAEWf_U8dZ1grUnEDeYZp1emPE3Rr8Ya_cc')

users = []

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Рассылка')
    item2 = types.KeyboardButton('Оставить заявку')
    item3 = types.KeyboardButton('Отозвать заявку')
    item4 = types.KeyboardButton('Ссылка на сайт')

    markup.add(item1, item2, item3, item4)

    #Внести пользователя в базу даннных    
    #if(not BotDB.user_exists(message.from_user.id)):
    #    BotDB.add_user(message.from_user.id)
        
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup = markup)
    


@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Пример заявки':
            bot.send_message(message.from_user.id, '''1.Название команды, цифра и буква класса -  *Спортсмены* 10 И\n2.Состав команды - фамилия, имя(6 основных, один на лавке запасных, по желанию)''')
        elif message.text == 'Рассылка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('+')  
            item2 = types.KeyboardButton('-')
            back = types.KeyboardButton('<- Назад')
            markup.add(item1, item2, back)
        
            bot.send_message(message.chat.id, 'Рассылка', reply_markup = markup)
        
        elif message.text == 'Оставить заявку':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Оставить заявку')
            item2 = types.KeyboardButton('')
            back = types.KeyboardButton('<- Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, '''Пример заявки\n
            1.Название команды, цифра и буква класса -  *Спортсмены* 10 И\n
            2.Состав команды - фамилия, имя(6 основных, один на лавке запасных, по желанию)''', reply_markup = markup)

        elif message.text == 'Отозвать заявку':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Отозвать заявку')
            item2 = types.KeyboardButton(' ')
            back = types.KeyboardButton('<- Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Отозвать заявку', reply_markup = markup)
        
        elif message.text == 'Ссылка на сайт':
            bot.send_message(message.chat.id, 'Наш сайт 7645754765346543')
        
        elif message.text == '<- Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Рассылка')
            item2 = types.KeyboardButton('Оставить заявку')
            item3 = types.KeyboardButton('Отозвать заявку')
            item4 = types.KeyboardButton('Ссылка на сайт')

            markup.add(item1, item2, item3, item4,)

            bot.send_message(message.chat.id, '<- Назад', reply_markup = markup)

        elif message.text == '+':
            user = message.chat.id
            if user not in users:
                users.append(user)
            bot.send_message(user, "max loh")
            
        
        elif message.text == '-':
            user = message.chat.id
            users.remove(user)
            bot.send_message(user, "Все, все.")
            

        


def spam():
    global users
    while True:
        for user in users:
            bot.send_message(user, "max loh")
        time.sleep(1200)

spam_thread = Thread(target=spam)
spam_thread.start()

bot.polling(none_stop=True)
