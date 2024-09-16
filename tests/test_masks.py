import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    return [
        7000792289606361,  # Вводимое значение для первого теста
        0,  # Вводимое значение для второго теста (для проверки пустыми)
        700079228960636100,  # Вводимое значение для третьего теста
    ]


@pytest.fixture
def expected_results():
    return [
        "7000 79** **** 6361",  # Ожидаемый результат для первого теста
        ValueError,  # Ожидаемое исключение для второго теста
        ValueError,  # Ожидаемое исключение для третьего теста
    ]


def test_get_mask_card_number(card_numbers, expected_results):
    for card_number, expected in zip(card_numbers, expected_results):
        if expected is ValueError:
            with pytest.raises(ValueError):
                get_mask_card_number(card_number)
        else:
            result = get_mask_card_number(card_number)
            assert result == expected


@pytest.fixture
def account_numbers():
    return [
        73654108430135874305,  # Вводимое значение для первого теста
        0,  # Вводимое значение для второго теста (для проверки пустыми)
        700079228960636100,  # Вводимое значение для третьего теста
    ]


@pytest.fixture
def expected_results_account_user():
    return [
        "7365 41** **** 4305",  # Ожидаемый результат для первого теста (обновлен)
        ValueError,  # Ожидаемое исключение для второго теста
        ValueError,  # Ожидаемое исключение для третьего теста
    ]


def test_get_mask_account_number(account_numbers, expected_results_account):
    for account_number, expected in zip(account_numbers, expected_results_account):
        if expected is ValueError:
            with pytest.raises(ValueError):
                get_mask_account(account_number)
        else:
            result = get_mask_account(account_number)
            assert result == expected
