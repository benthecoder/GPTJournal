# GPTJournal

A Telegram bot that uses the ChatGPT api to organize your thoughts

## Why

I write my daily thoughts at the end of the day and often times I forget what I did. Having this bot can allow me to easily jot down my thoughts throughout the day and also have gpt prompt me to go deeper into my thoughts.

I was inspired by this article [GPT-3 Is the Best Journal I've Ever Used](https://every.to/chain-of-thought/gpt-3-is-the-best-journal-you-ve-ever-used) and this page [Daily Notes | jxnl.co](https://www.jxnl.co/notes)

## How it will work

I'll send text messages to the bot and it will respond with a prompts to get me thinking more.

At the end of the day, it will summarize and organize my thoughts and upload it to my Notion page

## TODO

- [ ] add example user and assistant messages for better prompts as shown [here](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb)

## Setup

### Creating Telegram bot

1. Sign up for telegram
1. Open Telegram and type @BotFather in search bar
1. Hit the Start Button
1. Send command `/newbot` to create a new bot
1. Follow prompts to set a name and username
1. Save the token for later

### Setup flask app

1. Rename `.env.local.example` to `.env`
2. create python environemnt `python3 -m venv venv`
3. activate environment `source venv/bin/activate`
4. install dependencies `pip install -r requirements.txt`

### Setup the ChatGPT api

1. In `gpt.py` file, customize the SYSTEM prompt to your liking

### Deploy to vercel

1. sign in with Github
2. import this git repository
3. set env variables
4. hit Deploy

Limits of the [hobby plan](https://vercel.com/docs/concepts/limits/overview#general-limits)

### setup webhooks

1. run `python app.py` to set the vercel url as the webhook

### setup notion

1. Create a new integration and get the token [(guide)](https://developers.notion.com/docs/create-a-notion-integration)
2. Get database_id of the database you want to add to [(guide)](https://developers.notion.com/docs/working-with-databases#adding-pages-to-a-database)
3. Add both to `.env` file

## References

Flask and Vercel

- [jxnl/vercel-telegram-gpt: Flask app deployed via Vercel to respond to messages via GPT](https://github.com/jxnl/vercel-telegram-gpt)

ChatGPT

- [openai-cookbook/How_to_format_inputs_to_ChatGPT_models.ipynb](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb)
- [Instructing chat models](https://platform.openai.com/docs/guides/chat/instructing-chat-models)
- [minimaxir/chatgpt_api_test: Demos utilizing the ChatGPT API](https://github.com/minimaxir/chatgpt_api_test)
- [Create completion](https://platform.openai.com/docs/api-reference/completions/create)

Datetime

- [How do I get a value of datetime.today() in Python that is "timezone aware"? - Stack Overflow](https://stackoverflow.com/questions/4530069/how-do-i-get-a-value-of-datetime-today-in-python-that-is-timezone-aware)

Notion

- [How to work with the Notion API in Python - Python Engineer](https://www.python-engineer.com/posts/notion-api-python/)
- [Create new integrations](https://www.notion.so/my-integrations)
- [Finding database_id](https://developers.notion.com/docs/working-with-databases#adding-pages-to-a-database)
- [Block](https://developers.notion.com/reference/block)
- [Create a page](https://developers.notion.com/reference/post-page)
