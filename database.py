#-*- coding: utf-8 -*-

import sqlite3


class DatabaseManager:
    def __init__(self):
        pass

    def get_message_with_id(self, id):
        """
        Получение сообщения по его id
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

    def get_buttons(self):
        """
        Получение всех кнопок
        :param none
        :return cortege
        """
        connect = sqlite3.connect("data.db")
        with connect:
            cursor = connect.cursor()
            result = cursor.execute("""
                    SELECT row, text
                    FROM markup
                """).fetchall()

        return result

    def get_admins(self):
        """
        Получение идентификаторов всех аккаунтов
        у который есть доступы к админ панели
        :param none
        :return cortege
        """
        connect = sqlite3.connect("data.db")
        with connect:
            cursor = connect.cursor()
            result = cursor.execute("""
                    SELECT user_id
                    FROM admins
                """).fetchall()

        return result[0]

    def add_admin(self, user_id):
        """
        Добавляет нового пользователя в таблицу админов
        :param user_id
        :return none
        """
        connect = sqlite3.connect("data.db")
        with connect:
            cursor = connect.cursor()
            cursor.execute("""
                    INSERT INTO admins
                    (user_id)
                    VALUES 
                    ( ? )
                """, (user_id, ))

            connect.commit()
