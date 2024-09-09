def get_mask_card_number(card_number: int) -> str:
    """Преобразуем номер карты в строку"""
    card_number_str = str(card_number)
    # Создаем маску: оставляем первые 6 символов, затем заменяем на *, и оставляем последние 4 символа
    masked_card_number_str = card_number_str[:6] + "*" * 6 + card_number_str[-4:]
    # Разделяем строку на группы по 4 символа
    masked_card_number = [masked_card_number_str[i : i + 4] for i in range(0, len(masked_card_number_str), 4)]
    # Объединяем группы с пробелами
    return " ".join(masked_card_number)


print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: int) -> str:
    """Преобразуем номер счета в строку"""
    account_number_str = str(account_number)
    # Создаем маску: первые символы заменяем на две *, и оставляем последние 4 символа
    masked_account_number = "*" * 2 + account_number_str[-4:]
    return masked_account_number


print(get_mask_account(73654108430135874305))
