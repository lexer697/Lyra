# utils.py
import asyncio
import random

async def human_typing_simulation(client, chat_id, text):
    """
    This simulates human typing delay before sending a message.
    """
    # Calculate delay based on message length
    delay = max(1, len(text) / 15)  # roughly 15 chars per second
    await client.send_chat_action(chat_id, "typing")
    await asyncio.sleep(delay)
    await client.send_message(chat_id, text)

def format_reply(text):
    """
    Optional: Format reply with emojis or extra style.
    """
    # You can add emojis or small tweaks here
    return f"💬 {text}"
