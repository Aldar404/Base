import requests
import random
import telebot
from telebot import types
import config2
from bs4 import BeautifulSoup

URL = 'https://baneks.ru/'


def parser(url):
    """
    парсит сайт с анекдотами
    :param url: baneks.ru сайт с анекдотами
    :return: текст анекдота
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    anekdots = soup.find('p')
    return anekdots.get_text('\n', strip=True)


bot = telebot.TeleBot(config2.TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Что бы поорать, отправь /jokes")


@bot.message_handler(commands=['jokes'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    memes = types.KeyboardButton('Jokes')
    markup.add(memes)
    bot.send_message(message.chat.id, 'Нажимай', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() == 'jokes':
        bot.send_message(message.chat.id, parser(f'{URL}{random.randint(1, 1100)}'))
    else:
        bot.send_message(message.chat.id, "Введи /jokes")


bot.polling(skip_pending=True)

