from src import masks
import pytest
from typing import Any, Dict,List

def test_get_mask_card_number() -> Any:
    assert masks.get_mask_card_number('1234567890123456') == "1234 56** **** 3456"
    assert masks.get_mask_card_number('6378387226255637') == "6378 38** **** 5637"
    assert masks.get_mask_account('1234567890123456') == "**3456"

@pytest.mark.parametrize(
    "number, expected",
    [
        ("1234534267890123456", "**3456"),
        ("1234567890123456", "**3456" ),
        ("567890123456", "**3456")
    ]
)

def test(number: str, expected:str) -> Any:
    assert masks.get_mask_account(number) == expected
