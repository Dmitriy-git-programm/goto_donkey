import time
import telebot
import random
import pytz
from datetime import datetime
from threading import Thread
from config import token


bot = telebot.TeleBot(token=token)

users = set()

screams = ['felix_blume_animals_donkey_braying_loudly_field_village.ogg',
           'felix_blume_animals_donkey_braying_close_up.ogg']


@bot.message_handler(commands=['start', 'help'])
def start(message):
    user = message.chat.id
    users.add(user)
    bot.send_message(user, "🐴 Привет, я осел из головинки.")


@bot.message_handler(commands=['stop'])
def remove_user(message):
    user = message.chat.id
    if user in users:
        users.remove(user)
    bot.send_message(user, "Ыа 🐴")


def spam():
    hour = (datetime.now(pytz.UTC).hour + 3) % 24
    if 5 < hour < 21:
        while True:
            for user in users:
                bot.send_voice(user, open(random.choice(screams), 'rb'))
            time.sleep(random.randint(900, 5400))


def polling():
    bot.polling(none_stop=True)


polling_thread = Thread(target=polling)
spam_thread = Thread(target=spam)

polling_thread.start()
spam_thread.start()
