from pyrogram import Client

api_id = 24561506
api_hash = '63793d001d59e795a83739a5076c8a77'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр - это id чата или имя получателя.
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message('@edim_sha', 'Куку! а я это сообщение отправил с помощью бота, вот так вот!')
app.stop()
мой токен котик обормотик - 6009940554:AAE9PoT-goc1e80BRmqOsUzKqosJ_Q0Gtms
после bot втыкаешь токен, полученный от тг фазер., чат_ид - ид, которые уже нажал старт в боте, и в конце сообщение бота
https://api.telegram.org/bot6009940554:AAE9PoT-goc1e80BRmqOsUzKqosJ_Q0Gtms/sendMessage?chat_id=950139404&text=hello!
