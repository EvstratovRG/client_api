import requests

from telegram import Bot


bot = Bot(token='6009940554:AAE9PoT-goc1e80BRmqOsUzKqosJ_Q0Gtms')

URL = 'https://api.thecatapi.com/v1/images/search'

chat_id = '950139404'
response = requests.get(URL).json()
random_cat_url = response[0].get('url')
bot.send_photo(chat_id, random_cat_url)
