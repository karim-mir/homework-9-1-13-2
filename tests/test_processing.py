import pytest
from datetime import datetime
from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date


# Тесты для filter_by_state
@pytest.mark.parametrize(
    "input_data, state, expected_output",
    [
        # Тестирование с разными значениями state
        (
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 2, "state": "CANCELED"},
                {"id": 3, "state": "EXECUTED"},
            ],
            "EXECUTED",
            [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}],
        ),
        (
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 2, "state": "CANCELED"},
                {"id": 3, "state": "EXECUTED"},
            ],
            "CANCELED",
            [{"id": 2, "state": "CANCELED"}],
        ),
        (
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 2, "state": "CANCELED"},
            ],
            "FAILED",
            [],
        ),  # Не существует 'FAILED'
    ],
)
def test_filter_by_state(input_data, state, expected_output):
    assert filter_by_state(input_data, state) == expected_output


# Тесты для sort_by_date
def test_sort_by_date():
    input_data = [
        {"id": 1, "date": "2021-01-01T12:00:00"},
        {"id": 2, "date": "2020-01-01T12:00:00"},
        {"id": 3, "date": "2021-01-01T12:00:00"},  # Одинаковая дата
        {"id": 4, "date": "2019-01-01T12:00:00"},
    ]

    expected_output_desc = [
        {"id": 1, "date": "2021-01-01T12:00:00"},
        {"id": 3, "date": "2021-01-01T12:00:00"},
        {"id": 2, "date": "2020-01-01T12:00:00"},
        {"id": 4, "date": "2019-01-01T12:00:00"},
    ]

    expected_output_asc = [
        {"id": 4, "date": "2019-01-01T12:00:00"},
        {"id": 2, "date": "2020-01-01T12:00:00"},
        {"id": 1, "date": "2021-01-01T12:00:00"},
        {"id": 3, "date": "2021-01-01T12:00:00"},
    ]

    assert sort_by_date(input_data) == expected_output_desc  # По умолчанию убывание
    assert sort_by_date(input_data, reverse=False) == expected_output_asc  # Сортировка по возрастанию


# Тесты на обработку некорректного формата даты
def test_sort_by_date_invalid_format():
    input_data = [
        {"id": 1, "date": "invalid-date"},
        {"id": 2, "date": "2020-01-01T12:00:00"},
    ]

    with pytest.raises(ValueError):
        sort_by_date(input_data)
