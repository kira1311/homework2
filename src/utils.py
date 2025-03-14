import json

import os


def read_operations_from_json(file_path):
    """ Если файл не существует, сразу возвращаем пустой список"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        return []
    except:
        return []
