import os
import flask
import telebot

from dotenv import load_dotenv
from gpt import ChatGPT
from pprint import pprint

load_dotenv()
gpt = ChatGPT()

app = flask.Flask(__name__)
bot = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"], threaded=False)


@app.route("/")
def hello():
    return {"status": "ok"}


# Process webhook calls
@app.route("/webhook", methods=["POST"])
def webhook():
    if flask.request.headers.get("content-type") == "application/json":
        json_string = flask.request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ""
    else:
        flask.abort(403)


@bot.message_handler(commands=["hi"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? Start chating with me!")


@bot.message_handler(commands=["end"])
def bye(message):
    bot.reply_to(message, gpt.end_chat())


@bot.message_handler(func=lambda message: True, content_types=["text"])
def chat(message):
    """Generate a response to a user-provided message"""
    response = gpt(message.text)
    bot.reply_to(message, response)


if __name__ == "__main__":
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    bot.remove_webhook()
    bot.set_webhook(url="https://gpt-journal-benthecoder.vercel.app/webhook")
