import pytest

from src.utils.json_utils import same_keys


@pytest.mark.parametrize(
    "first_dict,second_dict,has_same_keys",
    [
        ({}, {}, True),
        ({"key1": "value1"}, {"key1": "value1"}, True),
        ({"key2": "value1"}, {"key1": "value2"}, False),
        ({"key1": {}}, {"key1": {}}, True),
        ({"key1": {"Hola": 1}}, {"key1": {"Hola": 1}}, True),
        ({"key1": {"Hola": 1}}, {"key1": 1}, False),
        ({"key1": {"Hola": 1}}, {"key1": {"Adios": 1}}, False),
        ({"key1": {"Hola": 1, "Hola2": 1}}, {"key1": {"Hola": 1, "Hola2": 1}}, True),
        (
            {"key1": {"Hola": 1, "Hola2": 1, "Hola3": 1}},
            {"key1": {"Hola": 1, "Hola2": 1}},
            False,
        ),
    ],
)
def test_same_keys(first_dict: dict, second_dict: dict, has_same_keys: bool):
    assert same_keys(first_dict, second_dict) == has_same_keys
