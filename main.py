import os
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from openai import OpenAI

# Load .env variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not TELEGRAM_BOT_TOKEN or not GROQ_API_KEY:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or GROQ_API_KEY in .env")

# Initialize Groq API client
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

# In-memory chat history
class Reference:
    def __init__(self):
        self.response = ""

reference = Reference()
model = "llama3-70b-8192"

# Initialize bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Commands
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("👋 Welcome! I'm a Groq-powered LLaMA3 bot. Ask me anything.")

@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "📌 *Commands:*\n"
        "/start - Begin a new chat\n"
        "/clear - Clear previous memory\n"
        "/help - Show this message\n\n"
        "💬 Just send your question!",
        parse_mode="Markdown"
    )

@dp.message(Command("clear"))
async def clear_handler(message: Message):
    reference.response = ""
    await message.answer("🧹 Conversation cleared.")

# Main chat handler
@dp.message()
async def message_handler(message: Message):
    user_input = message.text
    print(f">>> USER: {user_input}")

    try:
        messages = []
        if reference.response:
            messages.append({"role": "assistant", "content": reference.response})
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        reference.response = reply
        print(f">>> BOT: {reply}")
        await message.answer(reply[:4096])

    except Exception as e:
        print(f"❌ Groq API error: {e}")
        await message.answer("⚠️ Groq API failed to respond.")

# Entrypoint
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
