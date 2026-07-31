from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from services.groq_service import get_ai_response
from services.memory import clear_history
from services.user_service import is_new_user
from config import BOT_TOKEN
from utils.helpers import send_long_message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    user_id = update.effective_user.id

    if is_new_user(user_id):
        text = f"""👋 Welcome {user}!

🤖 Main AI Assistant hoon.

💬 Mujhse Hindi, Hinglish aur English me baat kar sakte ho.

📝 Commands:
/help - Help
/about - About
/clear - Clear Memory

Bas message bhejo aur baat shuru karo. 😊"""
    else:
        text = f"""👋 Welcome Back {user}! 😊

Main phir se ready hoon.
Bas apna message bhejo."""

    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ Bas mujhe koi bhi question bhejo, main answer dunga."
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Telegram Bot\nVersion: 1.0"
    )


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    clear_history(user_id)

    await update.message.reply_text(
        "✅ Conversation memory cleared."
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_id = update.effective_user.id

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing",
    )

    ai_reply = get_ai_response(user_id, user_message)

    await send_long_message(update, ai_reply)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("✅ Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()