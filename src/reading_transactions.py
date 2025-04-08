import csv
import pandas as pd
from typing import List, Dict, Any

def read_transactions_csv(filename: str) -> List[Dict[str, Any]]:
    """
    Читает данные из CSV-файла и возвращает их в виде списка словарей.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def read_transactions_excel(filename: str) -> List[Dict[str, Any]]:
    """
    Читает данные из Excel-файла и возвращает их в виде списка словарей.
    """
    df = pd.read_excel(filename)
    data = df.to_dict(orient='records')
    return data

