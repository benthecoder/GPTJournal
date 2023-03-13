import os
import flask
import telebot

from dotenv import load_dotenv
from gpt import ChatGPT
from notion import create_page


load_dotenv()

app = flask.Flask(__name__)
bot = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"], threaded=False)
gpt = ChatGPT()


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


@bot.message_handler(commands=["start"])
def start(message):
    """Send a message when the command /start is issued."""
    bot.reply_to(
        message,
        "Hi there! Start by typing anything :)",
    )


@bot.message_handler(commands=["echo"])
def echo(message):
    """Echo the user message"""
    bot.reply_to(message, message.text)


@bot.message_handler(commands=["summarize"])
def summarize(message):
    """Summarize the conversation and upload conversation to Notion"""
    title = gpt("Summarize our conversation today in 10 words")
    messages = gpt.messages
    response = ""
    for message in messages[1:]:
        response += f"{message['role']}: {message['content']} \n\n"

    page = create_page(title, response)

    if page:
        bot.reply_to(message, f"Successfully created page titled: {title}")


@bot.message_handler(commands=["debug"])
def total_messages(message):
    bot.reply_to(message, len(gpt.messages))


@bot.message_handler(func=lambda message: True, content_types=["text"])
def chat(message):
    """Generate a response to a user-provided message"""
    response = gpt(message.text)
    bot.reply_to(message, response)


if __name__ == "__main__":
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    bot.remove_webhook()
    bot.set_webhook(url="https://gpt-journal-benthecoder.vercel.app/webhook")
