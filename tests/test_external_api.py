import unittest
from unittest.mock import MagicMock, patch

import requests

from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_convert_to_rub_success(self, mock_get):
        # Имитация успешного ответа от API
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 70.5}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = convert_to_rub(100, "USD")
        self.assertEqual(result, 70.5)

    @patch("src.external_api.requests.get")
    def test_convert_to_rub_failed_request(self, mock_get):
        # Имитация ошибки запроса к API
        mock_get.side_effect = requests.RequestException("Network error")

        result = convert_to_rub(100, "USD")
        self.assertEqual(result, 0.0)

    def test_convert_to_rub_with_rub(self):
        result = convert_to_rub(100, "RUB")
        self.assertEqual(result, 100.0)


if __name__ == "__main__":
    unittest.main()
