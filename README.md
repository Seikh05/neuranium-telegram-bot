# 🤖 Groq Telegram Bot

A blazing-fast Telegram chatbot powered by Groq (OpenAI-compatible) using LLaMA3.

## Features
- Groq API (llama3-70b-8192 by default)
- Commands: `/start`, `/clear`, `/help`
- Memory for contextual replies
- Aiogram + asyncio based

## Deploy to Railway
1. Push this repo to GitHub
2. Go to [Railway](https://railway.app/)
3. Create new project → Connect GitHub → Select this repo
4. Add environment variables:
   - `TELEGRAM_BOT_TOKEN`
   - `GROQ_API_KEY`
5. Deploy and done ✅
