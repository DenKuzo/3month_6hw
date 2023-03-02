from aiogram import executor  # для запуска бота
from handler import client, call_back, admin, fsm_anketa, extra
from config import db
import logging

client.register_handlers_client(db)
call_back.register_handlers_callback(db)
admin.register_handlers_admin(db)
fsm_anketa.register_handlers_anketa(db)
extra.register_handlers_extra(db)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)