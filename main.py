# main.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import config

# -----------------------------
# Telegram Client Setup
# -----------------------------
bot = Client(
    "ChatGPTBot",
    bot_token=config.BOT_TOKEN
)

# -----------------------------
# Start Command Handler
# -----------------------------
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(config.START_BUTTON_TEXT, url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")]
        ]
    )
    await message.reply(config.START_MESSAGE, reply_markup=keyboard)

# -----------------------------
# ChatGPT Response Handler
# -----------------------------
@bot.on_message(filters.private)
async def chat_response(client, message):
    user_text = message.text
    if not user_text:
        return

    # Call OpenAI API
    headers = {
        "Authorization": f"Bearer {config.OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_text}],
        "temperature": 0.7
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response_json = response.json()
        reply_text = response_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        reply_text = "⚠️ Something went wrong. Please try again."

    await message.reply(reply_text)

# -----------------------------
# Run Bot
# -----------------------------
print("🤖 Bot is starting...")
bot.run()
