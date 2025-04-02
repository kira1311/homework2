import re
from collections import Counter


def re_sort(list_transactions, search):
    """Эта функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    pattern = re.compile(search, re.IGNORECASE)
    operations = [operations for operations in list_transactions if pattern.search(operations.get("description", ""))]
    return operations


def count_category_dict(operations, category_op):
    """Эта функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает
     словарь."""
    descriptions = [op.get("description", "") for op in operations]
    counted = Counter()
    for category in category_op:
        counted[category] = sum(category in desc for desc in descriptions)
    return dict(counted)