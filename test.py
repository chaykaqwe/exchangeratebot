import aiohttp
import asyncio

API_KEY = 'ВАШ_API_КЛЮЧ'  # <-- Замени на свой ключ

async def get_usd_to_rub(amount_usd):
    url = f"https://api.currencyfreaks.com/latest?apikey={API_KEY}&symbols=RUB"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                usd_to_rub = float(data["rates"]["RUB"])
                converted = amount_usd * usd_to_rub
                print(f"\nКурс USD к RUB: {usd_to_rub}")
                print(f"{amount_usd} USD = {converted:.2f} RUB")
            else:
                print("Ошибка при получении данных:", response.status)

async def main():
    try:
        user_input = input("Введите сумму в USD: ")
        amount = float(user_input)
        await get_usd_to_rub(amount)
    except ValueError:
        print("Ошибка: введите корректное число.")

# Запуск
asyncio.run(main())