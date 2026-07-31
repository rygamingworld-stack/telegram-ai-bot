from groq import Groq
from services.memory import add_message, get_history
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def get_ai_response(user_id: int, message: str):
    try:
        add_message(user_id, "user", message)

        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Reply naturally in the same language as the user."
            }
        ]

        messages.extend(get_history(user_id))

        chat = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        reply = chat.choices[0].message.content

        add_message(user_id, "assistant", reply)

        return reply

    except Exception:
        return "⚠️ AI is temporarily unavailable. Please try again later."