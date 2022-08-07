#cd .git/Projects/Lessons/1/3_portfolio_project
'''хочу записать бот который убирает или добавляет кнопки, заходя в которые,
человек будет видить свои напоминания связанные дескрипшеном этой кнопки. Или сможет
под тему дескрипшена кнопки добавить еще кнопки со своими подтемами. Тем самым делать
себе напоминания или сложную, ветвистую структуру поднапоминаний'''

import telebot
from telebot import types
import config
import pandas as pd


#the tag bot's
bot = telebot.TeleBot('5314339897:AAHdJtEBtaMJ7VVlwwL5KtVb-Li65nAdI9k')


class Class_bot():

    def __init__():
        pass


    @bot.message_handler(commands=['start'])
    def main_bord(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bttn_CreateReminder = types.KeyboardButton("Создать напоминание")
        bttn_DeleteReminder = types.KeyboardButton("Удалить напоминание")
        bttn_WatchReminders = types.KeyboardButton("Посмотреть напоминания")
        bttn_AboutBot = types.KeyboardButton("О боте")
        markup.add(bttn_CreateReminder, bttn_AboutBot, bttn_DeleteReminder, bttn_WatchReminders)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! \
Я тестовый бот.".format(message.from_user), reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def text_message(message):

        if(message.text == "О боте"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bttn_MyName = types.KeyboardButton("Как меня зовут?")
            bttn_Abyll = types.KeyboardButton("Смысл бота")
            bttn_comeback = types.KeyboardButton("Вернуться в меню")
            markup.add(bttn_MyName, bttn_Abyll, bttn_comeback)
            bot.send_message(message.chat.id, text="Мы расскажим о наших \
безумных способностях =)", reply_markup=markup)


        elif(message.text == "Как меня зовут?"):
            bot.send_message(message.chat.id, "У меня нет имени, {0.first_name}. \
Но мы работаем над этим.".format(message.from_user))

        elif message.text == "Смысл бота":
            bot.send_message(message.chat.id, text="Поздороваться с \
пользователем и быть \"пока\" что сырым. ;-). В будущем ты \
сможешь добавлять напоминания удалять и следить за ними. Не спрашивай, \
я сам пока точно не знаю как оно будет выглядить.)))")

        elif (message.text == "Вернуться в меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bttn_CreateR = types.KeyboardButton("Создать напоминание")
            bttn_DeleteReminder = types.KeyboardButton("Удалить напоминание")
            bttn_WatchReminders = types.KeyboardButton("Посмотреть напоминания")
            bttn_AboutBot = types.KeyboardButton("О боте")
            markup.add(bttn_CreateR, bttn_AboutBot, bttn_DeleteReminder, bttn_WatchReminders)
            bot.send_message(message.chat.id, text="Привет, {0.first_name}! \
Я тестовый бот.".format(message.from_user), reply_markup=markup)

        elif (message.text == "Создать напоминание"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bttn_CreateR = types.KeyboardButton("Создать")
            bttn_WatchMenu = types.KeyboardButton("Вернуться в меню")
            markup.add(bttn_CreateR, bttn_WatchMenu)
            bot.send_message(message.chat.id, text="Напишите название напоминания \
(желательно короткое)", reply_markup=markup)

        elif (message.text == "Создать"):
            bot.send_message(message.chat.id, text="<<<")

        else:
            bot.send_message(message.chat.id, text="На такую комманду я не заскриптовал.")
            #message.from_user.username нужно добавить в SQL

bot.polling(none_stop=True)

if __name__ == '__main__':
    application()
