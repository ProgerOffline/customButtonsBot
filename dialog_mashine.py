#-*- coding: utf-8 -*-

from aiogram.dispatcher.filters.state import State, StatesGroup


class DialogMashine(StatesGroup):
    add_admin = State()