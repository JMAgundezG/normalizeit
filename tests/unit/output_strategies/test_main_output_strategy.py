"""Test main output strategy."""

import pytest

from src.output_strategies.main_output_strategy import MainOutputStrategy


@pytest.mark.parametrize(
    "normalized_data,output_scheme,output_data",
    [
        ({}, {}, {}),
        ({"$$value": "value1"}, {"key1": "$$value"}, {"key1": "value1"}),
        (
            {"$$value": "value1", "$$value2": "aa"},
            {"key1": "$$value", "key2": "$$value2"},
            {"key1": "value1", "key2": "aa"},
        ),
        (
            {"$$value": "value1"},
            {"key1": "$$notthesamekey"},
            {"key1": "$$notthesamekey"},
        ),
        (
            {"$$value": {"key11": "value1"}},
            {"key1": "$$value"},
            {"key1": {"key11": "value1"}},
        ),
        (
            {"$$value": "value1"},
            {"key1": {"key11": "$$value"}},
            {"key1": {"key11": "value1"}},
        ),
    ],
)
def test_output_strategy(normalized_data: dict, output_scheme: dict, output_data: dict):
    """
    Test output strategy. It should return the same data as the input data.
    """
    assert (
        MainOutputStrategy().write_output(normalized_data, output_scheme) == output_data
    )
