#-*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext


class MashineHandlers:
    def __init__(self, bot, dp, db, dialog_mashine, keyboards):
        self.bot = bot
        self.dp = dp 
        self.db = db
        self.dialog_mashine = dialog_mashine
        self.keyboards = keyboards

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

        # Изменение текста на кнопке
        @self.dp.message_handler(state=self.dialog_mashine.edit_text)
        async def process_edit_btn(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                btn_id = data['btn_id']

            self.db.change_button_text_with_id(btn_id, message.text)
            await self.bot.send_message(
                    chat_id=message.chat.id,
                    text=self.db.get_message_with_id("9"),
                    reply_markup=self.keyboards.edit_buttons(),
                )

            await state.finish()


        # Изменение сообщения, которое присылает кнопка
        @self.dp.message_handler(state=self.dialog_mashine.edit_message)
        async def process_edit_btn(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                btn_id = data['btn_id']

            self.db.change_button_message_with_id(btn_id, message.text)
            await self.bot.send_message(
                    chat_id=message.chat.id,
                    text=self.db.get_message_with_id("9"),
                    reply_markup=self.keyboards.edit_buttons(),
                )

            await state.finish()