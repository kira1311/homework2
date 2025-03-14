import logging
import os
import json


if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/utils.log', mode='w')
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def read_operations_from_json(file_path):
    """ Если файл не существует, сразу возвращаем пустой список"""
    logger.info(f"загрузка транзакций из файла {data_path}")
    if not os.path.exists(file_path):
        logger.error(f"файл {data_path} не найден")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            logger.info(f"файл {data_path} загружен успешно")
            return data
        return []
    except:
        return []


data_path = 'data/operations.json'
print(read_operations_from_json(data_path))
