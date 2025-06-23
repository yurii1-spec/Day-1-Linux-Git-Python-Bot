import telebot
TOKEN = '7764666872:AAH0gI-WQGXiL2uI84K0SkmP0F3QHyPDfqI'
bot= telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Hey! I`m a DeutschNinjaBot 🤖")

bot.polling()
