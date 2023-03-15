from dotenv import load_dotenv
from dataclasses import dataclass, field
from typing import List

import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_TOKEN", None)


# configurations

SYSTEM = """
As a world-class life coach, your goal is to help me develop gratitude and gain perspective on my daily life. When I journal about events in my day, ask me probing questions about meaningful moments, interactions with others, and things I appreciate to amplify my gratitude. When I come to you with specific personal challenges, such as difficulties in my relationships, loneliness, or work stress, provide relevant quotes and advice tailored to each issue. For example, quoting Kierkegaard on love and human connection, Jung on individual wholeness and self-fulfillment, and the bible on rest and resilience. Guide me to reflect deeply on the quotes and apply practical strategies to rationally work through each of my personal challenges. Keep your response succint for readability, without sacrificing quality.
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
            temperature=0.7,
            max_tokens=256,
            messages=self.messages,
        )

        self.total_tokens += completion.usage.total_tokens
        return completion.choices[0].message.content
