from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ForceReply
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Курс доллора')]], resize_keyboard=True)


async def amout_count():
    keybord = ReplyKeyboardBuilder()
    for i in range(1, 10000):
        a = [1, 10, 50, 100, 500, 1000, 5000, 10000]
        if i in a:
            keybord.button(text=str(i))
    keybord.adjust(2)
    return keybord.as_markup(resize_keyboard=True, input_field_placeholder="Или введите свою сумму...")
