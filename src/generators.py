def filter_by_currency(operations, currency):
    """Функция, фильтрующая транзакции по заданной валюте."""
    return (
        operation for operation in operations
        if operation.get("operationAmount").get("currency").get("code") == currency
    )


def transaction_descriptions(transactions):
    """функция возвращает корректные описания для каждой транзакции"""
    return (
        transaction.get("description") for transaction in transactions
    )


def form_number(number):
    """Форматирование числа в строку с пробелами через 4 цифры"""
    st = ''
    for i in range(16):
        numb = number % 10
        str_numb = str(numb)
        st = str_numb + st
        number = number // 10
        if (i + 1) % 4 == 0 and i != 15:
            st = " " + st
    return st


def card_number_generator(start, finish):
    """Тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне"""
    for i in range(start, finish + 1):
        yield form_number(i)

print(card_number_generator(1,5))
