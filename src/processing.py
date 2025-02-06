from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    """
    return sorted(
        data, key=lambda x: datetime.fromisoformat(x["date"]) if x.get("date") else datetime.min, reverse=descending
    )
