import telebot

TOKEN = "8330008814:AAFy8Pg23dTYidV3M7wxMjCTHqw7p0w5HXE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot is running 24/7 🔥")

bot.infinity_polling()
