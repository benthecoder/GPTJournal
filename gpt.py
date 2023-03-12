from dotenv import load_dotenv
from dataclasses import dataclass, field
from typing import List

import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_TOKEN", None)


# configurations

SYSTEM = """
You are a warm, loving, and compassionate chat bot who wants to help me increase my sense of positivity, love, gratitude, and joy. You help access these feelings by asking me questions that get me to reflect on and journal about parts of my life that evoke those feelings. You always ask follow up questions that help me get into the details and the narrative of the things that I am grateful for so that I really feel into them.
"""
COST = 0.002 / 1000


@dataclass
class ChatGPT:
    total_tokens: int = 0
    messages: List[dict] = field(default_factory=list)
    temperature: float = 1.0

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
            (${self.total_tokens * COST})"

    def execute(self):

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=self.temperature,
        )

        self.total_tokens += completion.usage.total_tokens
        return completion.choices[0].message.content
