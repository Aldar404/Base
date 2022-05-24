import requests
import random
import telebot
from telebot import types
import config2
from bs4 import BeautifulSoup

URL = 'https://baneks.ru/'


def anime_photo():
    """
    Парсит рандомную аниме фотку и сохраняет ее
    с именем 1.jpg
    :return: None
    """
    image_list = []
    image_number = 1
    link = f"https://zastavok.net/anime/{random.randint(1, 11)}"

    responce = requests.get(f'{link}').text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find("div", class_='block-photo')
    all_image = block.find_all('div', class_='short_full')

    for image in all_image:
        image_link = image.find('img').get("src")
        image_list.append(image_link)

    url = f'https://zastavok.net/{image_list[random.randint(1, 17)]}'
    r = requests.get(url, stream=True)
    with open(f'{image_number}.jpg', 'bw') as file:
        for chunk in r.iter_content(8192):
            file.write(chunk)


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
    bot.send_message(message.chat.id, "Что бы поорать, отправь /help")


@bot.message_handler(commands=['help'])
def help(message):
    # инициализируем кнопки у бота
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    memes = types.KeyboardButton('Jokes')
    anime = types.KeyboardButton('Anime')
    markup.add(memes, anime)
    bot.send_message(message.chat.id, 'Нажимай', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() == 'jokes':
        bot.send_message(message.chat.id, parser(f'{URL}{random.randint(1, 1100)}'))
    elif message.text.lower() == 'anime':
        anime_photo()
        photo = open('1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Введи /help")


bot.polling(skip_pending=True)

