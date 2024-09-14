from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    :param data: Список словарей, который нужно фильтровать.
    :param state: Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.
    :return: Новый список словарей, содержащих только те, у которых ключ 'state' соответствует заданному значению.
    """
    return [item for item in data if item.get("state") == state]


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
