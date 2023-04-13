import logging

from logging.handlers import RotatingFileHandler


logging.basicConfig(
    level=logging.DEBUG,
    filemode='w',
    encoding='utf-8',
    filename='program.log',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# asctime — время события,
# levelname — уровень важности,
# message — текст сообщения,
# name — имя логгера.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    'my_logger.log', maxBytes=50000000, backupCount=5
)
logger.addHandler(handler)
logging.debug('123')  # Когда нужна отладочная информация
logging.info('Сообщение отправлено')  # Когда нужна дополнительная информация
logging.warning('Большая нагрузка!')  # Когда что-то идёт не так, но работает
logging.error('Бот не смог отправить сообщение')  # Когда что-то сломалось
logging.critical('Всё упало! Зовите админа!1!111')  # Когда всё совсем плохо

handler.setFormatter(formatter)
