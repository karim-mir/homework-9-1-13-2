import os

import pytest

from src.decorators import log


# Удаление файла журнала после выполнения теста
@pytest.fixture
def clean_up():
    yield
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")


@log("test_log.txt")
def divide(x, y):
    return x / y


def test_log_written_to_file(clean_up):
    divide(10, 2)

    # Подождите некоторое время или проверяйте существование файла
    assert os.path.exists("test_log.txt"), "Файл журнала не создан."

    with open("test_log.txt", "r") as file:
        logs = file.readlines()

    assert any(
        "Запуск функции: divide с аргументами: (10, 2), {}" in log for log in logs
    ), "Логи выполнения не найдены."
    assert any("Функция: divide вернула: 5.0" in log for log in logs), "Логи результата не найдены."


def test_log_error(clean_up):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    with open("test_log.txt", "r") as file:
        logs = file.readlines()

    assert any("Ошибка в функции: divide с аргументами: (10, 0), {}" in log for log in logs)
