import csv
import json
import re
from datetime import datetime
from typing import Dict, List

import pandas as pd

# Пути к файлам
json_path = "data/transactions.json"
excel_path = "C:/Users/zheba/Downloads/transactions_excel.xlsx"
csv_path = "C:/Users/zheba/AppData/Local/Programs/Python/Python312/Homework_1/src/data/transactions.csv"


def get_financial_transactions(path: str) -> List[Dict]:
    """Функция принимает путь к файлу CSV в качестве аргумента и выдает список словарей с транзакциями"""
    transactions = []
    with open(path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")  # Указываем ; как разделитель
        for row in reader:
            transactions.append(row)
            print(
                row.get("id", "ID отсутствует"),
                row.get("state", "Статус отсутствует"),
                row.get("date", "Дата отсутствует"),
                row.get("amount", "Сумма отсутствует"),
                row.get("currency_name", "Имя валюты отсутствует"),
                row.get("currency_code", "Код валюты отсутствует"),
                row.get("from", "Отправитель отсутствует"),
                row.get("to", "Получатель отсутствует"),
                row.get("description", "Описание отсутствует"),
            )
    return transactions


def get_financial_transactions_operations(path: str) -> List[Dict]:
    """Функция для считывания финансовых операций из Excel и возвращает список словарей с транзакциями."""
    df = pd.read_excel(path)
    operations = []

    for index, row in df.iterrows():
        operation = {
            "id": row.get("id"),
            "state": row.get("state"),
            "date": row.get("date"),
            "amount": row.get("amount"),
            "currency_name": row.get("currency_name"),
            "currency_code": row.get("currency_code"),
            "from": row.get("from"),
            "to": row.get("to"),
            "description": row.get("description"),
        }
        operations.append(operation)

    return operations


def filter_transactions(transactions: List[Dict[str, any]], search_term: str) -> List[Dict[str, any]]:
    """Фильтрует список банковских операций по заданной строке поиска."""
    pattern = re.compile(search_term, re.IGNORECASE)
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]

    return filtered_transactions


def sort_transactions(transactions: List[Dict], order: str) -> List[Dict]:
    return sorted(
        transactions,
        key=lambda x: datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=(order == "по убыванию"),
    )


def filter_by_currency(transactions: List[Dict], currency: str) -> List[Dict]:
    return [t for t in transactions if t.get("currency_code") == currency]


def print_transactions(transactions: List[Dict[str, any]]):
    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(
                f"{transaction.get('date', 'Дата отсутствует')} "
                f"{transaction.get('description', 'Описание отсутствует')}"
            )
            amount = transaction.get("amount", "Сумма отсутствует")
            currency_code = transaction.get("currency_code", "Код валюты отсутствует")
            print(f"Сумма: {amount} {currency_code}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из Excel-файла")
    print("3. Получить информацию о транзакциях из CSV-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        with open(json_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)
    elif choice == "2":
        print("Для обработки выбран Excel-файл.")
        transactions = get_financial_transactions_operations(excel_path)
    elif choice == "3":
        print("Для обработки выбран CSV-файл.")
        transactions = get_financial_transactions(csv_path)
    else:
        print("Неверный выбор.")
        return

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): "
        ).upper()

        filtered_transactions = [t for t in transactions if str(t.get("state", "")).upper() == status]

        if filtered_transactions:
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    # Сортировка по дате
    sort_decision = input("Программа: Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_decision == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию? ").strip()
        filtered_transactions = sort_transactions(filtered_transactions, order)

    # Фильтрация по валюте
    currency_decision = input("Программа: Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_decision == "да":
        filtered_transactions = filter_by_currency(filtered_transactions, "RUB")

    # Дополнительная фильтрация по описанию
    description_decision = (
        input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    )
    if description_decision == "да":
        search_term = input("Введите слово для поиска: ")
        filtered_transactions = filter_transactions(filtered_transactions, search_term)

    print("Распечатываю итоговый список транзакций...")
    print_transactions(filtered_transactions)


if __name__ == "__main__":
    main()
