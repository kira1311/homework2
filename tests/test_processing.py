from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми транзакциями (ISO 8601 даты)."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
    ],
)
def test_filter_by_state(sample_transactions: List[Dict[str, Any]], state: str, expected_count: int) -> None:
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected_count
    assert all(tx["state"] == state for tx in result)


def test_filter_by_state_empty() -> None:
    assert sort_by_date([]) == []
