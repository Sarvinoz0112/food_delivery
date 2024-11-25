from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def generate_main_menu():
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="Katigoriyalar")
    )
    builder.row(
        KeyboardButton(text="Sozlamalar"),
        KeyboardButton(text="Buyurtmalar tarixi")
    )

    return builder.as_markup(resize_keyboard=True)