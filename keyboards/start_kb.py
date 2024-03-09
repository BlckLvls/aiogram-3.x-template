from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Кнопка 1", callback_data="btn1"))
    kb.row(InlineKeyboardButton(text="Кнопка 2", callback_data="btn2"))

    return kb.as_markup()
