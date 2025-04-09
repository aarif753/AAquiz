import telebot
import os

BOT_TOKEN = os.getenv('AAGmCDQVRJX41GI72g5YFjl2r3ilHaMqO8g')

bot = telebot.TeleBot(AAGmCDQVRJX41GI72g5YFjl2r3ilHaMqO8g)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user
    with open("userdata.txt", "a") as f:
        f.write(f"ID:{user.id} | Username:@{user.username} | Name:{user.first_name} {user.last_name}\n")
    bot.reply_to(message, f"Hi {user.first_name}! Welcome to AA1 Mini App Bot.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
