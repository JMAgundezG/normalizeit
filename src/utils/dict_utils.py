"""
This module contains functions to work with dicts
"""


def _keys_dict_1_in_dict_2(dict_1: dict, dict_2: dict) -> bool:
    """Check if the keys from dict_1 are in dict_2"""
    for key, value in dict_1.items():
        if not isinstance(value, dict):
            if key not in dict_2.keys():
                return False
        else:
            if not isinstance(dict_2[key], dict):
                return False
            if not _keys_dict_1_in_dict_2(value, dict_2[key]):
                return False
    return True


def same_keys(d_1: dict, d_2: dict) -> bool:
    """Check if 2 dicts has the same keys"""
    return _keys_dict_1_in_dict_2(d_1, d_2) and _keys_dict_1_in_dict_2(d_2, d_1)
