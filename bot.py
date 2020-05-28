import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('C:/Users/adm.a.danyliuk/Desktop/telegram_bot/sticker/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомне число")
    item2 = types.KeyboardButton("Як справи?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Вітаю {0.first_name}! \n Я -  {1.first_name}, Бот створений як піддослідний кролик".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомне число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == "Як справи?":
            bot.send_message(message.chat.id, 'Круто, в тебе як?')
        else:
            bot.send_message(message.chat.id, 'Хмм навіть незнаю')

#RUN
bot.polling(none_stop=True)