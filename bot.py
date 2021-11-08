#-*- coding: utf-8 -*-

from aiogram import Bot
from aiogram import types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database import DatabaseManager
from keyboards import KeyboardsManager
from dialog_mashine import DialogMashine

TOKEN = "1614502276:AAFGR_oVKF89-KyrZDKrO5ryeF24yf8Icro"


class CustomBot:
	def __init__(self, token):
		self.bot = Bot(token)
		self.dp = Dispatcher(self.bot,  storage=MemoryStorage())

		self.db = DatabaseManager()
		self.keyboards = KeyboardsManager(self.db)
		self.dialog_mashine = DialogMashine()

	def start(self):
		# Главное меню
		@self.dp.message_handler(commands=['start'])
		async def process_start(message: types.Message):
			await self.bot.send_message(
					chat_id=message.chat.id,
					text=self.db.get_message_with_id("1"),
					reply_markup=self.keyboards.main(),
				)

		# Админ панель, для редактирвания элементов
		@self.dp.message_handler(commands=['admin'])
		async def process_admin(message: types.Message):
			admins = self.db.get_admins()
			if str(message.chat.id) in admins:
				await self.bot.send_message(
						chat_id=message.chat.id,
						text=self.db.get_message_with_id("2"),
					)

			else:
				await self.bot.send_message(
						chat_id=message.chat.id,
						text=self.db.get_message_with_id("3"),
					)

		# Процесс добавления нового админа
		@self.dp.message_handler(commands=['addAdmin'])
		async def process_add_admin(message: types.Message):
			admins = self.db.get_admins()
			if str(message.chat.id) in admins:
				await self.bot.send_message(
						chat_id=message.chat.id,
						text=self.db.get_message_with_id("4"),
					)

			else:
				await self.bot.send_message(
						chat_id=message.chat.id,
						text=self.db.get_message_with_id("3"),
					)

		executor.start_polling(self.dp, skip_updates=True)


if __name__ == "__main__":
	token = "1614502276:AAFGR_oVKF89-KyrZDKrO5ryeF24yf8Icro"
	bot = CustomBot(token)
	bot.start()