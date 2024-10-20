import unittest
from unittest.mock import mock_open, patch

import pandas as pd

# Предполагаем, что ваш код находится в файле src/main.py
from src.main import (filter_by_currency, filter_transactions, get_financial_transactions,
                      get_financial_transactions_operations, print_transactions, sort_transactions)


class TestFinancialFunctions(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description"
        "\n1;EXECUTED;2023-10-01T21:27:25.241689;1000;Ruble;RUB;Account A;Account B;Payment for service",
    )
    def test_get_financial_transactions(self, mock_file):
        transactions = get_financial_transactions("dummy_path.csv")
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["amount"], "1000")

    @patch("pandas.read_excel")
    def test_get_financial_transactions_operations(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame(
            {
                "id": [1],
                "state": ["EXECUTED"],
                "date": ["2023-10-01T21:27:25.241689"],
                "amount": [1000],
                "currency_name": ["Ruble"],
                "currency_code": ["RUB"],
                "from": ["Account A"],
                "to": ["Account B"],
                "description": ["Payment for service"],
            }
        )

        transactions = get_financial_transactions_operations("dummy_path.xlsx")
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["amount"], 1000)

    def test_filter_transactions(self):
        transactions = [{"description": "Payment for service"}, {"description": "Refund for service"}]
        filtered = filter_transactions(transactions, "Payment")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["description"], "Payment for service")

    def test_sort_transactions(self):
        transactions = [{"date": "2023-10-01T21:27:25.241689"}, {"date": "2022-10-01T21:27:25.241689"}]
        sorted_transactions = sort_transactions(transactions, "по возрастанию")
        self.assertEqual(sorted_transactions[0]["date"], "2022-10-01T21:27:25.241689")

    def test_filter_by_currency(self):
        transactions = [{"currency_code": "RUB"}, {"currency_code": "USD"}]
        filtered = filter_by_currency(transactions, "RUB")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["currency_code"], "RUB")

    @patch("builtins.print")  # Мокаем функцию print, чтобы предотвратить вывод на экран
    def test_print_transactions(self, mock_print):
        transactions = [
            {
                "date": "2023-10-01T21:27:25.241689",
                "description": "Payment for service",
                "amount": "1000",
                "currency_code": "RUB",
            }
        ]
        print_transactions(transactions)
        mock_print.assert_any_call("Всего банковских операций в выборке: 1")
        mock_print.assert_any_call("2023-10-01T21:27:25.241689 Payment for service")
        mock_print.assert_any_call("Сумма: 1000 RUB")


if __name__ == "__main__":
    unittest.main()
