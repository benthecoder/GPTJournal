import os
import telebot

from dotenv import load_dotenv

load_dotenv()


bot = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"], threaded=False)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
