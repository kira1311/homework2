import json
import csv
import pandas as pd
import re


def load_json(filename):
    """Загрузка данных из JSON-файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_csv(filename):
    """Загрузка данных из библиотеки CSV"""
    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def load_xlsx(filename):
    """Загрузка данных из библиотеки pandas"""
    df = pd.read_excel(filename)
    return df.to_dict(orient='records')


# Функции фильтрации
def search_transactions(transactions, search_str):
    """Фильтрация транзакций по строке в описании"""
    pattern = re.compile(search_str, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def filter_by_status(transactions, status):
    """Фильтрация транзакций по статусу"""
    status = status.lower()
    return [transaction for transaction in transactions if transaction.get('status', '').lower() == status]


def sort_transactions(transactions, reverse=False):
    """Сортировка транзакций по дате"""
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)


def main():
    """Диалог с пользователем для выбора нужного файла"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите файл для загрузки данных:")
    print("1. JSON")
    print("2. CSV")
    print("3. XLSX")

    file_choice = input("Ваш выбор: ")
    if file_choice == '1':
        filename = input("Введите имя JSON-файла: ")
        transactions = load_json(filename)
    elif file_choice == '2':
        filename = input("Введите имя CSV-файла: ")
        transactions = load_csv(filename)
    elif file_choice == '3':
        filename = input("Введите имя XLSX-файла: ")
        transactions = load_xlsx(filename)
    else:
        print("Неверный выбор.")
        return

    if not transactions:
        print("Не удалось загрузить данные. Завершаем работу.")
        return

    print(f"Данные из файла {filename} загружены.")

    status = input("Введите статус (EXECUTED, CANCELED, PENDING) для фильтрации: ").lower()
    filtered_transactions = filter_by_status(transactions, status)

    sort_choice = input("Хотите отсортировать по дате (да/нет)? ").strip().lower()
    if sort_choice == 'да':
        sort_order = input("По возрастанию или по убыванию? ").strip().lower()
        reverse = sort_order == 'по убыванию'
        filtered_transactions = sort_transactions(filtered_transactions, reverse)

    search_choice = input("Хотите искать транзакции по слову в описании (да/нет)? ").strip().lower()
    if search_choice == 'да':
        search_str = input("Введите слово для поиска: ")
        filtered_transactions = search_transactions(filtered_transactions, search_str)

    if filtered_transactions:
        print("Распечатываю список транзакций...")
        for transaction in filtered_transactions:
            print(f"{transaction.get('date')} - {transaction.get('description')} - {transaction.get('amount')}")
    else:
        print("Не найдено подходящих транзакций.")


main()
