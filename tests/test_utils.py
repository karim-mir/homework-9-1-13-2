import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):
    """Класс для тестирования функции load_transactions."""

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_load_transactions_single_entry(self, mock_open, mock_exists):
        """Тестирование загрузки файла с одной транзакцией."""
        mock_exists.return_value = True  # Настраиваем мок для существования файла

        result = load_transactions("data/transactions.json")

        self.assertEqual(len(result), 1)  # Проверяем количество загруженных транзакций
        self.assertEqual(result[0]["id"], 1)  # Проверяем корректность id
        self.assertEqual(result[0]["amount"], 100)  # Проверяем корректность amount

    @patch("os.path.exists")
    def test_load_transactions_file_not_found(self, mock_exists):
        """Тестирование поведения при отсутствии файла."""
        mock_exists.return_value = False  # Настраиваем мок для несуществующего файла

        result = load_transactions("data/transactions.json")

        self.assertEqual(result, [])  # Ожидаем пустой список

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="not a json string")
    def test_load_transactions_invalid_json(self, mock_open, mock_exists):
        """Тестирование обработки некорректного JSON."""
        mock_exists.return_value = True  # Настраиваем мок для существования файла

        result = load_transactions("data/transactions.json")

        self.assertEqual(result, [])  # Ожидаем пустой список

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='{"not": "a list"}')
    def test_load_transactions_data_not_a_list(self, mock_open, mock_exists):
        """Тестирование, когда загруженные данные не являются списком."""
        mock_exists.return_value = True  # Настраиваем мок для существования файла

        result = load_transactions("data/transactions.json")

        self.assertEqual(result, [])  # Ожидаем пустой список

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_transactions_empty_file(self, mock_open, mock_exists):
        """Тестирование обработки пустого файла."""
        mock_exists.return_value = True  # Настраиваем мок для существования файла

        result = load_transactions("data/transactions.json")

        self.assertEqual(result, [])  # Ожидаем пустой список

    @patch("os.path.exists")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"id": "a", "amount": 100}]',
    )
    def test_load_transactions_invalid_id_type(self, mock_open, mock_exists):
        """Тестирование некорректного типа id."""
        mock_exists.return_value = True  # Настраиваем мок для существования файла

        result = load_transactions("data/transactions.json")

        self.assertEqual(result, [])  # Ожидаем пустой список

    @patch("os.path.exists")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"id": 1, "amount": "not a number"}]',
    )
    def test_load_transactions_invalid_amount_type(self, mock_open, mock_exists):
        """Тестирование некорректного типа amount."""
        mock_exists.return_value = True  # Настраиваем мок для существования файла

        result = load_transactions("data/transactions.json")

        self.assertEqual(result, [])  # Ожидаем пустой список


if __name__ == "__main__":
    unittest.main()
