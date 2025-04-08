from src.reading_transactions import read_transactions_csv, read_transactions_excel
from src.utils import read_operations_from_json
from src.processing import filter_by_state, sort_by_date
from src.bank_operations import filter_by_currency, search_transactions
from src.utils import get_date, mask_account_card

def main():
    print("С каким файлом работаем?")
    print("1 - JSON, 2 - CSV, 3 - XLSX")

    while True:
        choice = input("Введите номер: ")
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            file_name = 1
            trans = read_operations_from_json("data/operations.json")
            break
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            file_name = 2
            trans = read_transactions_csv("data/transactions.csv")
            break
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            file_name = 3
            trans = read_transactions_excel("data/transactions_excel.xlsx")
            break
        else:
            print("Такого выбора нет.")

    while True:
        print("Сортировать по возрастанию/убыванию? (Введите: 'по возрастанию' или 'по убыванию')")
        user_input = input().lower()
        if user_input == "по возрастанию":
            trans = sort_by_date(trans, False)
            break
        elif user_input == "по убыванию":
            trans = sort_by_date(trans, True)
            break
        else:
            print("Нет такого ответа.")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            trans = filter_by_currency(trans, "RUB")
            break
        elif user_input == "нет":
            break
        else:
            print("Нет такого ответа.")

    # Пример поиска по слову
    while True:
        print("Отфильтровать по слову в описании? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            word = input("Введите слово: ")
            trans = search_transactions(trans, word)
            break
        elif user_input == "нет":
            break
        else:
            print("Нет такого ответа.")

    # Пример фильтра по состоянию
    trans = filter_by_state(trans)

    # Печать результата
    print("Распечатываю итоговый список транзакций...")
    if len(trans) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"Всего банковских операций в выборке: {len(trans)}\n")
    for tx in trans:
        date_str = get_date(tx.get("date"))
        desc = tx.get("description", "")

        if desc == "Открытие вклада":
            mask_to = mask_account_card(tx.get("to"))
        else:
            mask_from = mask_account_card(tx.get("from"))
            mask_to = mask_account_card(tx.get("to"))

        # Пример вывода суммы в зависимости от типа файла:
        if file_name == 1:
            op_amount = tx.get("operationAmount", {})
            amount = op_amount.get("amount", "???")
            currency_name = op_amount.get("currency", {}).get("name", "???")
            summa = f"{amount} {currency_name}"
        else:
            amount = tx.get("amount", "???")
            currency = tx.get("currency_code", "???")
            summa = f"{amount} {currency}"

        # Вывод строки
        if desc == "Открытие вклада":
            print(f"{date_str} {desc}\n{mask_to}\nСумма: {summa}\n")
        else:
            print(f"{date_str} {desc}\n{mask_from} -> {mask_to}\nСумма: {summa}\n")

if __name__ == '__main__':
    main()
