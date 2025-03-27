import csv
import pandas as pd
import os


def read_transactions_csv(file_csv):
    """Считывает фин. операции из CSV"""
    transactions = []

    if not os.path.exists(file_csv):
        print(f"Ошибка: Файл '{file_csv}' не найден.")
        return transactions

    try:
        with open(file_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")

    return transactions


def read_transactions_excel(file_xlsx):
    """Считывает фин. операции из Excel"""
    transactions = []

    if not os.path.exists(file_xlsx):
        print(f"Ошибка: Файл '{file_xlsx}' не найден.")
        return transactions

    try:
        data_frame = pd.read_excel(file_xlsx)
        transactions = data_frame.to_dict(orient='records')
    except Exception as e:
        print(f"Ошибка при чтении Excel файла: {e}")

    return transactions
