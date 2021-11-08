#-*- coding: utf-8 -*-

from aiogram import types


class KeyboardsManager:
    def __init__(self, db):
        self.db = db

    def main(self):
        """
        Главная клавиатура
        :param none
        :return keyboard
        """
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        
        buttons = self.db.get_buttons()
        for button in buttons:
            btn = types.KeyboardButton(
                    text=button[1],
                )
            keyboard.add(btn)

        return keyboard

    def admin(self):
        """
        Клавиатура админ панели
        :param none
        :return keyboard
        """
        keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

        btn1 = types.InlineKeyboardButton(
                text="Изменить кнопки",
                callback_data="admin:edit_buttons",
            )        

        btn2 = types.InlineKeyboardButton(
                text="Изменить сообщения",
                callback_data="admin:edit_messages",
            )

        keyboard.add(btn1, btn2)
        return keyboard