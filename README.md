# GPTJournal

A Telegram bot that uses GPT-3 to organize your thoughts

## Why

I write my daily thoughts at the end of the day and often times I forget what I did. Having this bot can allow me to easily jot down my thoughts throughout the day and also have gpt prompt me to go deeper into my thoughts.

I was inspired by this article [GPT-3 Is the Best Journal I've Ever Used](https://every.to/chain-of-thought/gpt-3-is-the-best-journal-you-ve-ever-used) and this page [Daily Notes | jxnl.co](https://www.jxnl.co/notes)

## How it will work

I'll send text messages (voice in a future development) to the bot and it will respond with a prompts to get me thinking more.

At the end of the day, it will summarize and organize my thoughts and upload it to my Notion page

## TODO

- [ ] setup flask
- [ ] setup vercel deployment
- [ ] write code to use openai chatgpt model for prompting
  - [ ] test the right prompt
  - references
    - [Chat completion - OpenAI API](https://platform.openai.com/docs/guides/chat)
    - [minimaxir/chatgpt_api_test: Demos utilizing the ChatGPT API](https://github.com/minimaxir/chatgpt_api_test)
- [ ] integrate with notion
  - [ ] get text throughout the day somehow
  - [ ] summarize it with gpt
  - [ ] upload to notion with title and content

## Setup

### Creating Telegram bot

1. Sign up for telegram
1. Open Telegram and search for @BotFather in search bar
1. Hit the Start Button
1. Send command `/newbot` to create a new bot
1. Follow prompts to set a name and username
1. Save the token

## References

- [jxnl/vercel-telegram-gpt: Flask app deployed via Vercel to respond to messages via GPT](https://github.com/jxnl/vercel-telegram-gpt)
