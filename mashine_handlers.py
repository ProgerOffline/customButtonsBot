#-*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext


class MashineHandlers:
    def __init__(self, bot, dp, db, dialog_mashine):
        self.bot = bot
        self.dp = dp 
        self.db = db
        self.dialog_mashine = dialog_mashine

    def handlers(self):
        """
        Обработка всех сотояний которые существуют
        """
        
        # Выдача доступа к админ панеле, новому пользователю
        @self.dp.message_handler(state=self.dialog_mashine.add_admin)
        async def process_add_admin(message: types.Message, state: FSMContext):
            await state.finish()

            self.db.add_admin(message.text)
            await self.bot.send_message(
                    chat_id=message.chat.id,
                    text=self.db.get_message_with_id("5"),
                )
