import json
import os
from unittest import mock


def read_operations_from_json(file_path):
    """Если файл отсутствует, немедленно возвращаем пустой список."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        return []
    except Exception as e:
        return []


def test_read_operations_from_json_success():
    """Тестирует успешное чтение данных из файла"""
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", '
        '"date": "2019-08-26T10:50:58.294041", '
        '"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, '
        '"description": "Перевод организации", "from": "Maestro 1596837868705199", '
        '"to": "Счет 64686473678894779589"}]'
    )

    with mock.patch("os.path.exists", return_value=True):
        with mock.patch("builtins.open", mock.mock_open(read_data=mock_data)):
            result = read_operations_from_json("fake_path.json")
    expected_result = json.loads(mock_data)
    assert result == expected_result


def test_file_not_found():
    """Тестирует поведение функции при отсутствии файла"""
    with mock.patch("os.path.exists", return_value=False):
        result = read_operations_from_json("non_existent_file.json")

    assert result == []


def test_json_decode_error():
    """Тестирует функцию при ошибке декодирования"""
    with mock.patch("os.path.exists", return_value=True):
        with mock.patch("builtins.open", mock.mock_open(read_data='{"id": 1, "amount": 100}')):
            with mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0)):
                result = read_operations_from_json("fake_path.json")

    assert result == []
