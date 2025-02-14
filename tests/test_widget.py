from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize(
    "number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361" ),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305" )
    ]
)

def test_mask_account_card(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected

@pytest.mark.parametrize(
    "number, expected",
    [
    ("2024-03-11T02:26:18.671407", "11.03.24")
    ]
)

def test_get_date(number: str, expected: str) -> None:
    assert get_date(number) == expected

@pytest.mark.parametrize("acc", ["", None, "abcd efgh", "1234", "111122223333"])

def test_mask_account_card_invalid(acc: str) -> None:

    with pytest.raises(ValueError):
        mask_account_card(acc)