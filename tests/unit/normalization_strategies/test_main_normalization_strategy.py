"""
Test main output strategy. 
"""

import pytest

from src.config.config import Config
from src.normalization_strategies.main_normalization_strategy import \
    MainNormalizationStrategy


@pytest.fixture
def normalization_strategy():
    return MainNormalizationStrategy(Config())


@pytest.mark.parametrize(
    "input_scheme,output_scheme,raw_data,normalized_data",
    [
        ({}, {}, {}, {}),
        (
            {"key1": "$$value"},
            {"keyoutput": "$$value"},
            {"key1": "outputvalue"},
            {"keyoutput": "outputvalue"},
        ),
        (
            {"key1": "$$value", "key2": "$$value2", "key3": {"key31": "$$valueinside"}},
            {"keyoutput": "$$value", "keyout2": "$$value2", "keyout3": "$$valueinside"},
            {
                "key1": "value1",
                "key2": {"dictvaluekey": "dictvaluevalue"},
                "key3": {"key31": "valueinside"},
            },
            {
                "keyoutput": "value1",
                "keyout2": {"dictvaluekey": "dictvaluevalue"},
                "keyout3": "valueinside",
            },
        ),
    ],
)
def test_normalization(
    input_scheme: dict,
    output_scheme: dict,
    raw_data: dict,
    normalized_data: dict,
    normalization_strategy: MainNormalizationStrategy,
):
    """
    Test fetch data method.
    """
    normalization_strategy.config.input_scheme = input_scheme
    normalization_strategy.config.output_scheme = output_scheme
    assert normalization_strategy.normalize(raw_data) == normalized_data
