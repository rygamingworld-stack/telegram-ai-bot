from telegram import Update


async def send_long_message(update: Update, text: str):
    MAX_LENGTH = 4000

    if len(text) <= MAX_LENGTH:
        await update.message.reply_text(text)
        return

    for i in range(0, len(text), MAX_LENGTH):
        await update.message.reply_text(text[i:i + MAX_LENGTH])