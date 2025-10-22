# handlers/start.py

from pyrogram import filters

async def start_command(client, message):
    text = (
        "👋 Hello! Main aapka Human-like ChatBot hoon.\n\n"
        "Type /chat <message> to start chatting with me.\n"
        "Type /help to see available commands."
    )
    await message.reply(text)
