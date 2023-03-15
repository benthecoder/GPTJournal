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
    convo = ""
    for m in gpt.messages[1:]:  # exclude system message
        convo += f"{m['role']}: {m['content']} \n\n"

    title = gpt("summarize our conversation so far in 10 words")

    page = create_page(title, convo)

    bot.reply_to(
        message,
        f"Saved our conversation to Notion :)" if page else "Failed to save :(",
    )


@bot.message_handler(commands=["debug"])
def total_messages(message):
    bot.reply_to(message, len(gpt.messages))


@bot.message_handler(commands=["t"])
def chat(message):
    """Generate a response to a user-provided message"""

    response = gpt(message.text)
    bot.reply_to(message, response)


if __name__ == "__main__":
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    bot.remove_webhook()
    bot.set_webhook(url="https://gpt-journal-benthecoder.vercel.app/webhook")
