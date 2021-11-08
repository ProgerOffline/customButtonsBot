#-*- coding: utf-8 -*-

import sqlite3


class DatabaseManager:
	def __init__(self):
		pass

	def get_message(self, id):
		"""
		Возвращает сообщение по его id
		:param id идентификатор сообщения
		:return str
		"""
		connect = sqlite3.connect("data.db")
		with connect:
			cursor = connect.cursor()
			result = cursor.execute("""
					SELECT text
					FROM messages
					WHERE id = ?
				""", (id, )).fetchone()

		return result[0]