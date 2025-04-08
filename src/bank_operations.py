import re

def sort_transactions(transactions: list, reverse=False) -> list:
    """Сортировка списка транзакций по дате (или по другому критерию)."""
    return sorted(transactions, key=lambda x: x.get('date'), reverse=reverse)

def filter_by_currency(transactions: list, currency_code: str) -> list:
    """Фильтрация транзакций по валюте."""
    return [t for t in transactions if t.get('currency_code') == currency_code]

def search_transactions(transactions: list, search_str: str) -> list:
    """Фильтрация по слову (подстроке) в описании."""
    pattern = re.compile(search_str, re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get('description', ''))]