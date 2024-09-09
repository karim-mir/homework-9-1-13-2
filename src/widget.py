from masks import get_mask_card_number, get_mask_account

def mask_account_card(card_details: str) -> str:
    """ Принимает строку с типом карты/счета и номером, возвращает замаскированный номер. """
    # Разделяем строку на части по пробелу
    parts = card_details.split()
    # Последняя часть это номер карты
    last_part = parts[-1]
    # Тип карты (Visa Platinum, Maestro и тп)
    card_or_account_type = ' '.join(parts[:-1])
    # В зависимости от типа переиспользуем функции
    if card_or_account_type.lower().startswith("счет"):
        masked_number = get_mask_account(int(last_part))
    else:
        masked_number = get_mask_card_number(int(last_part))
    # Возвращаем строку с замаскированным кодом
    return f"{card_or_account_type} {masked_number}"

print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date: str) -> str:
    """ Заменяем знак "-" в строке с датой на "." """
    new_get_date = date[:10].replace("-", ".")
    # Возвращаем новый формат даты
    return f"{new_get_date[8:10]}.{new_get_date[5:7]}.{new_get_date[:4]}"

print(get_date("2024-03-11T02:26:18.671407"))