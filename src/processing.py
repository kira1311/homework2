from datetime import datetime
from typing import List, Dict

def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует транзакции по состоянию."""
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data

def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортирует транзакции по дате."""
    # Функция для извлечения даты из элемента списка
    def get_date(transaction):
        date_str = transaction.get("date")
        if date_str:
            return datetime.fromisoformat(date_str)
        else:
            return datetime.min  # Возвращаем минимальную дату, если дата отсутствует

    # Сортируем данные по дате
    sorted_data = sorted(data, key=get_date, reverse=descending)
    return sorted_data
