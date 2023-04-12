import requests
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup


load_dotenv()
token = os.getenv('TOKEN')
url = os.getenv('URL')
updater = Updater(token)


def get_new_image():
    response = requests.get(url).json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat_id=chat.id, photo=get_new_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
        reply_markup=buttons
    )
    context.bot.send_photo(chat.id, get_new_image())


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

updater.start_polling()
updater.idle()
