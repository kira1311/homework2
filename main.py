import json
import csv
import pandas as pd
import re
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

def load_json(filename):
    """Загрузка данных из JSON-файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден. Пожалуйста, проверьте путь к файлу.")
        return []

def load_csv(filename):
    """Загрузка данных из CSV-файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден. Пожалуйста, проверьте путь к файлу.")
        return []

def load_xlsx(filename):
    """Загрузка данных из XLSX-файла"""
    try:
        df = pd.read_excel(filename)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден. Пожалуйста, проверьте путь к файлу.")
        return []

def search_transactions(transactions, search_str):
    """Фильтрация транзакций по строке в описании"""
    pattern = re.compile(search_str, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]

def filter_by_state(transactions, state):
    """Фильтрация транзакций по состоянию"""
    state = state.lower()
    filtered_transactions = []
    for transaction in transactions:
        # Проверяем, является ли 'state' строкой, прежде чем вызвать .lower()
        state_value = transaction.get('state', '')
        if isinstance(state_value, str) and state_value.lower() == state:
            filtered_transactions.append(transaction)
        elif isinstance(state_value, float) and str(state_value).lower() == state:
            filtered_transactions.append(transaction)
    return filtered_transactions

def sort_transactions(transactions, reverse=False):
    """Сортировка транзакций по дате"""
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)

def main():
    """Функция обработки данных и взаимодействия с пользователем"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        user_input = input()
        if user_input == "1":
            print("Для обработки выбран JSON-файл.")
            file_name = 1
            trans = load_json("data/operations.json")
            break
        elif user_input == "2":
            print("Для обработки выбран CSV-файл.")
            file_name = 2
            trans = load_csv("data/transactions.csv")
            break
        elif user_input == "3":
            print("Для обработки выбран XLSX-файл.")
            file_name = 3
            trans = load_xlsx("data/transactions_excel.xlsx")
            break
        else:
            print("Такого выбора нет.")

    while True:
        user_input = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING
            """
        ).upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            trans = filter_by_state(trans, user_input)
            break
        else:
            print(f"Статус операции {user_input} недоступен.")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            sort_date = True
            break
        elif user_input == "нет":
            sort_date = False
            break
        else:
            print("Нет такого ответа.")

    if sort_date:
        while True:
            print("Отсортировать по возрастанию или по убыванию? ")
            user_input = input().lower()
            if user_input == "по возрастанию":
                trans = sort_transactions(trans, False)
                break
            elif user_input == "по убыванию":
                trans = sort_transactions(trans, True)
                break
            else:
                print("Нет такого ответа.")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            trans = list(filter_by_currency(trans, "RUB"))
            break
        elif user_input == "нет":
            break
        else:
            print("Нет такого ответа.")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            user_input = input("Введите слово: \n")
            trans = search_transactions(trans, user_input)
            break
        elif user_input == "нет":
            break
        else:
            print("Нет такого ответа.")

    print("Распечатываю итоговый список транзакций...")
    if len(trans):
        print(f"Всего банковских операций в выборке: {len(trans)}\n")
        for date in trans:
            ye_mo_da = get_date(date.get("date"))
            desc = date.get("description")
            if date.get("description") == "Открытие вклада":
                mask_disc = mask_account_card(date.get("to"))
            else:
                mask_card = mask_account_card(date.get("from"))
                mask_disc = mask_account_card(date.get("to"))
            if file_name == 1:
                op_am = date.get("operationAmount")
                if op_am and op_am.get("currency"):
                    summa = f"Сумма: {op_am.get('amount')} {op_am.get('currency').get('name')}"
                else:
                    summa = "Сумма: Неизвестно"
            elif file_name == 2 or file_name == 3:
                summa = f"Сумма: {date.get('amount')} {date.get('currency_code')}"
            if date.get("description") == "Открытие вклада":
                print(f"{ye_mo_da} {desc}\n{mask_disc}\n{summa}\n")
            else:
                print(f"{ye_mo_da} {desc}\n{mask_card} -> {mask_disc}\n{summa}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

if __name__ == '__main__':
    main()
