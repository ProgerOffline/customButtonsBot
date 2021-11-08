#-*- coding: utf-8 -*-

from aiogram import types

class CallbackHandlers:
	def __init__(self, bot, dp, db, dialog_mashine):
		self.bot = bot
		self.dp = dp
		self.db = db
		self.dialog_mashine = dialog_mashine

	def handlers(self):
		@self.dp.callback_query_handler(lambda c: c.data)
		async def process_callback(call: types.CallbackQuery):
			print(f"Button pressed {call.data}")
			button = call.data

			if button.split(":")[0] == "admin":
				cmd = button.split(":")[1]

				if cmd == "edit_buttons":
					pass

				elif cmd == "edit_messages":
					pass
