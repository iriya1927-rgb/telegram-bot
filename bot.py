import telebot

TOKEN = "8330008814:AAFo5oVPZVtzrGBdnV2njXU8UmO70k3QmeE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot is running 24/7 🔥")

bot.infinity_polling()
