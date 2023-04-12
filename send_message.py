import telegram

TELEGRAM_TOKEN = '6009940554:AAE9PoT-goc1e80BRmqOsUzKqosJ_Q0Gtms'
CHAT_ID = '950139404'

bot = telegram.Bot(TELEGRAM_TOKEN)


def send_message(message):
    bot.send_message(CHAT_ID, message)


send_message('Приветствую!')
