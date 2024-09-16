def get_mask_card_number(card_number: int) -> str:
    """Преобразуем номер карты в строку с маской"""
    # Преобразуем номер карты в строку
    card_number_str = str(card_number)

    # Проверяем, состоит ли номер карты только из цифр и имеет ли нужную длину
    if not card_number_str.isdigit() or len(card_number_str) < 16 or len(card_number_str) > 19:
        raise ValueError("Введен некорректный номер карты")

    # Создаем маску: оставляем первые 6 символов, затем заменяем на *, и оставляем последние 4 символа
    masked_card_number_str = card_number_str[:6] + "*" * (len(card_number_str) - 10) + card_number_str[-4:]

    # Разделяем строку на группы по 4 символа
    masked_card_number = [masked_card_number_str[i : i + 4] for i in range(0, len(masked_card_number_str), 4)]

    # Объединяем группы с пробелами
    return " ".join(masked_card_number)


print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: int) -> str:
    """Преобразуем номер счета в строку"""
    account_number_str = str(account_number)

    # Проверяем, состоит ли номер карты только из цифр и имеет ли нужную длину
    if not account_number_str.isdigit() or len(account_number_str) < 16 or len(account_number_str) > 20:
        raise ValueError("Введен некорректный номер счета")

    # Создаем маску: первые символы заменяем на две *, и оставляем последние 4 символа
    masked_account_number = "*" * 2 + account_number_str[-4:]
    return masked_account_number


print(get_mask_account(73654108430135874305))
