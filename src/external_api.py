import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")

url = "https://api.apilayer.com/currency_data/convert"


def convert_to_rub(amount: float, currency: str) -> float:
    "Функция для конвертации валют в рубли"
    if currency == "RUB":
        return round(amount, 2)

    headers = {"apikey": EXCHANGE_API_KEY}
    params = {"amount": amount, "from": currency, "to": "RUB"}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return round(data["result"], 2)

    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return 0.0


if __name__ == "__main__":
    rub = convert_to_rub(100, "USD")
    print(f"Сумма в рублях: {rub}")
