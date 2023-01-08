"""
JSON Utils
"""
import json


def json_to_dict(json_str: str) -> dict:
    """Convert a json string to a dict"""
    return json.loads(json_str)
