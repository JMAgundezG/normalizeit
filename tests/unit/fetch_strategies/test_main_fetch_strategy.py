"""
Test main output strategy.
"""

import pytest

from src.fetch_strategies.main_fetch_strategy import MainFetchStrategy


@pytest.mark.parametrize(
    "raw_data,fetch_scheme,key,normalized_data",
    [
        ({}, {}, "$$", {}),
        ({"key1": "value1"}, {"key1": "$$value"}, "$$", {"$$value": "value1"}),
        ({"key1": "value1"}, {"key1": "$%value"}, "$%", {"$%value": "value1"}),
        ({"key1": "value1"}, {"key1": "value"}, "$%", {}),
        ({"key1": "value1"}, {}, "$%", {}),
        ({}, {"key1": "$%value"}, "$%", {}),
        (
            {"key1": {"key11": "value11"}},
            {"key1": "$%value"},
            "$%",
            {"$%value": {"key11": "value11"}},
        ),
        (
            {"key1": {"key11": "correctvalue"}},
            {"key1": {"key11": "$%value"}},
            "$%",
            {"$%value": "correctvalue"},
        ),
    ],
)
def test_fetch_data(
    raw_data: dict, fetch_scheme: dict, key: str, normalized_data: dict
):
    """
    Test fetch data method.
    """
    assert (
        MainFetchStrategy().fetch_data(raw_data, fetch_scheme, key) == normalized_data
    )
