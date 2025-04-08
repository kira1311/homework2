import json
from typing import List, Dict, Any

def read_operations_from_json(filename: str) -> List[Dict[str, Any]]:
    """
    Читает данные из JSON-файла и возвращает их в виде списка словарей.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_date(date_str: str) -> str:
    """
    Преобразует дату к нужному формату (или просто возвращает, 
    если не нужно менять).
    """
    return date_str

def mask_account_card(card_str: str) -> str:
    """
    Маскирует номер карты/счёта (например, оставить первые 4 и последние 4 цифры).
    """
    if not card_str:
        return "Неизвестная карта/счет"
    # Пример: "1234 56** **** 7890" или любая другая логика маскировки
    return card_str[:4] + "..." + card_str[-4:]