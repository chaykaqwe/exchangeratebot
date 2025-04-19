from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ForceReply
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выбрать валюту')]], resize_keyboard=True)


async def amout_count():
    keybord = ReplyKeyboardBuilder()
    for i in range(1, 10000):
        a = [1, 10, 50, 100, 500, 1000, 5000, 10000]
        if i in a:
            keybord.button(text=str(i))
    keybord.adjust(2)
    return keybord.as_markup(resize_keyboard=True, input_field_placeholder="Или введите свою сумму...")


async def currency_kb():
    currencys = {
        "Доллар США $": "USD",
        "Евро €": "EUR",
        "Российский рубль ₽": "RUB",
        "Британский фунт £": "GBP",
        "Японская иена ¥": "JPY",
        "Китайский юань ¥": "CNY",
        "Швейцарский франк ₣": "CHF",
        "Канадский доллар $": "CAD",
        "Австралийский доллар $": "AUD",
        "Новая турецкая лира ₺": "TRY",
        "Индийская рупия ₹": "INR",
        "Бразильский реал R$": "BRL",
        "Сингапурский доллар $": "SGD",
        "Норвежская крона kr": "NOK",
        "Шведская крона kr": "SEK",
        "Польский злотый zł": "PLN",
        "Украинская гривна ₴": "UAH",
        "Казахстанский тенге ₸": "KZT",
        "Гонконгский доллар $": "HKD",
        "Дирхам ОАЭ د.إ": "AED"
    }

    keybord = ReplyKeyboardBuilder()
    for key in currencys:
        keybord.button(text=str(key))
    keybord.adjust(5)
    return keybord.as_markup(resize_keyboard=True)
