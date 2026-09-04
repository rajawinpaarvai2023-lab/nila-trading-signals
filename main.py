import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 வணக்கம் நண்பா!\n\n"
        "🤖 Nila Trading Signals Bot தயாராக உள்ளது.\n\n"
        "📊 விரைவில் Trading Signal வசதிகள் சேர்க்கப்படும்.\n"
        "⚠️ இது Signal-only bot. தானாக Trade செய்யாது."
    )


@bot.message_handler(commands=["hello"])
def hello(message):
    bot.reply_to(message, "வணக்கம் நண்பா! 🤖")


print("Nila Trading Signals Bot is running...")

bot.delete_webhook(drop_pending_updates=True)
bot.infinity_polling()
