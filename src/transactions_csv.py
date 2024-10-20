import csv
from typing import Dict, List


def get_financial_transactions(path: str) -> List[Dict]:
    """Функция принимает путь к файлу CSV в качестве аргумента и выдает список словарей с транзакциями"""
    transactions = []
    with open(path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")  # Указываем ; как разделитель
        for row in reader:
            transactions.append(row)
            print(
                row["id"],
                row["state"],
                row["date"],
                row["amount"],
                row["currency_name"],
                row["currency_code"],
                row["from"],
                row["to"],
                row["description"],
            )
    return transactions


if __name__ == "__main__":
    path = "transactions.csv"
    transactions = get_financial_transactions(path)
