#-*- coding: utf-8 -*-

from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "1614502276:AAFGR_oVKF89-KyrZDKrO5ryeF24yf8Icro"


class CustomBot:
	def __init__(self, token):
		self.bot = Bot(token)
		self.dp = Dispatcher(self.bot,  storage=MemoryStorage())

	def start(self):
		@self.dp.message_handler(commands=['start'])
		async def process_start(message: types.Message):
			await self.bot.send_message(
					chat_id=message.chat.id,
					text=message.text,
				)

		executor.start_polling(self.dp, skip_updates=True)


if __name__ == "__main__":
	token = "1614502276:AAFGR_oVKF89-KyrZDKrO5ryeF24yf8Icro"
	bot = CustomBot(token)
	bot.start()