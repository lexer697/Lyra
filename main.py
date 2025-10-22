# main.py ke chat handler me replace kare:
from utils import human_typing_simulation, format_reply

@bot.on_message(filters.private)
async def chat_response(client, message):
    user_text = message.text
    if not user_text:
        return

    # OpenAI API call (same as before)
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
        import requests
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response_json = response.json()
        reply_text = response_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        reply_text = "⚠️ Something went wrong. Please try again."

    # Use utils for professional feel
    reply_text = format_reply(reply_text)
    await human_typing_simulation(client, message.chat.id, reply_text)
