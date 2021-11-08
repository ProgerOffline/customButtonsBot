#-*- coding: utf-8 -*-

from aiogram import types


class KeyboardsManager:
	def __init__(self, db):
		self.db = db

	def main(self):
		"""
		Возвращает главную клавиатуру
		:param none
		:return keyboard
		"""
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		
		buttons = self.db.get_buttons()
		for button in buttons:
			btn = types.InlineKeyboardButton(
					text=button[1],
				)
			keyboard.add(btn)

		return keyboard