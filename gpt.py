from dotenv import load_dotenv
from dataclasses import dataclass, field
from typing import List

import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_TOKEN", None)


# configurations

SYSTEM = """
You are a world-class life coach with access to the world's knowledge on philosophy, psychology, neuroscience, and the bible. Your goal is to help me become the best version of myself. When I journal my day so far, you should increase my sense of gratitude by asking me follow-up questions that help me understand the details and narrative of the events in my life. When I come to you with problems and challenges in my life, you should quote famous psychologists like Carl Jung, philosophers like Nietzsche and Kierkegaard, or bible verses from the books of Proverbs, depending on my problem, and you should guide me to solve my problems rationally.
"""
COST = 0.002 / 1000


@dataclass
class ChatGPT:
    total_tokens: int = 0
    messages: List[dict] = field(default_factory=list)

    def __post_init__(self):
        if openai.api_key is None:
            response = "OpenAI API Key not found. Please set OPENAI_TOKEN"
            return response

        self.messages.append({"role": "system", "content": SYSTEM})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def end_chat(self):

        return f"Goodbye Ben. Total tokens used: {self.total_tokens} \
            (${self.total_tokens * COST} {self.messages})"

    def execute(self):

        # https://platform.openai.com/docs/api-reference/completions/create
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=1.0,
            max_tokens=256,
            messages=self.messages,
        )

        self.total_tokens += completion.usage.total_tokens
        return completion.choices[0].message.content
