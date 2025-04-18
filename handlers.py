from aiogram import Router, F
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import aiohttp
import os
from datetime import datetime
import asyncio


load_dotenv()
router = Router(name=__name__)
API_KEY = os.getenv('API_KEY')
tasks = {}


@router.message(CommandStart())
async def cmd(mes: Message):
    await mes.answer('Добро пожаловать здесь вы можите смотреть курс валют!')


@router.message(F.text)
async def exchange_rate_usd(mes: Message):
    amount = int(mes.text)
    async with aiohttp.ClientSession() as session:
        url = f"https://api.currencyfreaks.com/latest?apikey={API_KEY}&symbols=RUB"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                usd_to_rub = data["rates"]["RUB"]
                convert = amount * float(usd_to_rub)
                await mes.answer(f"Курс доллара (USD) к рублю (RUB): {convert}")
            else:
                await mes.answer("Ошибка при получении данных:", response.status)
