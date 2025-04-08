import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")


def get_amount_rub(transaction):
    currency_code = transaction['operationAmount']['currency']['code']
    amount = float(transaction['operationAmount']['amount'])

    if currency_code == 'RUB':
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result["result"]
    else:
        print("Error: Unable to convert currency.")
        return None
