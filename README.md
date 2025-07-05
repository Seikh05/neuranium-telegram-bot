![Neuranium Bot](https://res.cloudinary.com/diqgquom2/image/upload/v1751744965/banner_d7owpn.png)

![Python](https://img.shields.io/badge/python-3.11+-blue?logo=python)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Powered by Groq](https://img.shields.io/badge/Groq-LLaMA3%2070B-red?logo=groq)
![Deployed on Railway](https://img.shields.io/badge/hosted%20on-Railway-1f425f?logo=railway)

# 🤖 Neuranium Telegram Bot

A blazing-fast AI-powered Telegram bot built using **LLaMA 3 via Groq**, deployed on **Railway**, and managed with **aiogram**.

Ask anything — get instant replies from a 70B parameter model.

---

## 🚀 Features

- ⚡️ Ultra-fast responses via [Groq API](https://groq.com/)
- 💬 Memory-enabled conversations
- 🛠️ Slash commands: `/start`, `/help`, `/clear`
- ☁️ Deployed on Railway
- 🔐 Secure with `.env` environment variables

---

## 🧰 Tech Stack

| Component     | Tech                |
|---------------|---------------------|
| Bot Framework | `aiogram`           |
| AI Model      | `Groq` + `LLaMA 3`  |
| Runtime       | `Python 3.11+`      |
| Deployment    | `Railway`           |
| Secrets       | `.env` + Railway Env Vars |

---

## ⚙️ Setup Locally

### 1. Clone the Repo

```bash
git clone https://github.com/Seikh05/neuranium-telegram-bot.git
cd neuranium-telegram-bot
````

### 2. Create `.env` File

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

### 3. Install & Run

```bash
python -m venv venv
source venv/bin/activate   # or .\venv\Scripts\activate on Windows

pip install -r requirements.txt
python main.py
```

---

## 🧪 Bot Commands

| Command     | Description                  |
| ----------- | ---------------------------- |
| `/start`    | Start the bot                |
| `/help`     | Show help info               |
| `/clear`    | Clear memory/conversation    |
| *(message)* | Get AI response from LLaMA 3 |

---

## ⚡️ One-Click Deploy (Railway)

Click the button below to deploy this bot instantly to Railway:

1. [Create a Railway project](https://railway.app/)
2. Link this GitHub repo
3. Add environment variables:

   * `TELEGRAM_BOT_TOKEN`
   * `GROQ_API_KEY`
4. Railway auto-installs from `requirements.txt` and runs `main.py` via `Procfile`

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙌 Credits

Built with ❤️ by [@Seikh05](https://github.com/Seikh05)

Powered by:

* [Groq](https://groq.com/)
* [Telegram](https://core.telegram.org/)
* [aiogram](https://docs.aiogram.dev/)
