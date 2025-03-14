import requests

from unittest.mock import patch


def get_amount_rub(transaction):
    """Функция для конвертации валюты"""
    currency_code = transaction['operationAmount']['currency']['code']
    amount = float(transaction['operationAmount']['amount'])

    if currency_code == 'RUB':
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    headers = {"apikey": "your_api_key_here"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result["result"]
    else:
        return []


def test_get_amount_rub_from_rub():
    transaction = {
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "RUB"}
        }
    }

    assert get_amount_rub(transaction) == 31957.58


@patch("requests.get")
def test_get_amount_rub_from_usd(mock_get):
    """Мокируем успешный ответ от API"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 435.649305}

    transaction = {
        "operationAmount": {
            "amount": "5",
            "currency": {"code": "USD"}
        }
    }

    assert get_amount_rub(transaction) == 435.649305


@patch("requests.get")
def test_get_amount_rub_exception(mock_get):
    """Мокируем ошибку от API"""
    mock_get.return_value.status_code = 500

    transaction = {
        "operationAmount": {
            "amount": "5",  # Сумма транзакции
            "currency": {"code": "USD"}
        }
    }

    assert get_amount_rub(transaction) == []
