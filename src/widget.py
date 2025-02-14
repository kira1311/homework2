from src import masks


def mask_account_card(acc: str) -> str:
    if not acc or not isinstance(acc, str):
        raise ValueError("Ошибка ввода. Ожидается строка с номером карты или счета.")

    number = "".join(filter(str.isdigit, acc))
    name_card = "".join(filter(lambda x: not x.isdigit(), acc)).strip()

    if len(number) in {16, 19}:
        masked_number = masks.get_mask_card_number(number)
    elif len(number) >= 20:
        masked_number = masks.get_mask_account(number)
    else:
        raise ValueError("Некорректный номер. Длина не соответствует картам или счетам.")

    return f"{name_card} {masked_number}".strip()

def get_date(date: str) -> str:
    date_form = f"{date[8:10]+'.'+date[5:7]+'.'+date[2:4]}"
    return date_form


