
import telebot
import datetime
import time
import threading
from keep_alive import keep_alive

TOKEN = '7745774473:AAEmyeCda2-PfLzarYabO0Cfe1F50VfHbJI'
CHAT_ID = 581391744

bot = telebot.TeleBot(TOKEN)

# Пример сообщений (можно заменить на JSON при необходимости)
scheduled_messages = [
    {
        "verse": "Псалом 27:1 — Господь свет мой и спасение моё: кого мне бояться?",
        "prayer": "Господи, наполни мой день миром и дай силы преодолеть всё. Аминь.",
        "reminder": "Ты не один. Бог с тобой, и каждый день — дар от Него.",
        "jarvis": "Доброе утро, Ден. Сегодня твой день. Бог с тобой, и я с тобой. Вперёд смело."
    }
]

def get_daily_content():
    content = scheduled_messages[0]
    return f"**{content['verse']}**\n\n{content['prayer']}\n\n_{content['reminder']}_\n\n*Jarvis:* {content['jarvis']}"

def send_daily_message():
    sent_today = None
    while True:
        now = datetime.datetime.now()
        weekday = now.weekday()
        hour = now.hour
        minute = now.minute
        date = now.date()
        if (weekday < 5 and hour == 6 and minute == 0) or (weekday >= 5 and hour == 8 and minute == 0):
            if sent_today != date:
                bot.send_message(CHAT_ID, get_daily_content(), parse_mode='Markdown')
                sent_today = date
            time.sleep(60)
        time.sleep(30)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Доброе утро! Я буду каждый день присылать тебе стихи, молитвы и слова от Jarvis.")

# Запуск
keep_alive()
threading.Thread(target=send_daily_message).start()
bot.polling()
