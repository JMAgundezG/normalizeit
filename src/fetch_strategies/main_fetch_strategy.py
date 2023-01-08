"""
This module contains the first defined fetching strategy.
"""

from src.utils.dict_utils import same_keys

from .fetch_strategy import FetchStrategy


class MainFetchStrategy(FetchStrategy):
    """
    First defined fetching strategy.
    """

    def fetch_data(
        self, dict_to_fetch: dict, fetch_schema: dict, identifier: str
    ) -> dict:
        """
        Fetches data from a dict using an input scheme given by parameter
        """
        data = {}
        print("FETCH SCHEMA", fetch_schema)
        print("DICT TO FETCH", dict_to_fetch)
        for key, value in fetch_schema.items():
            if identifier in value:
                print("KEY", key)
                print("dict_to_fetch", dict_to_fetch.keys())
                if key in dict_to_fetch.keys():
                    data[value] = dict_to_fetch[key]
                else:
                    print("Key not found")
            if isinstance(value, dict):
                data.update(self.fetch_data(dict_to_fetch[key], value, identifier))
        return data

    def validate(self, input_scheme: dict, dict_to_normalize: dict) -> bool:
        """
        Validate if the dict to normalize can be fetched using the input scheme
        """
        return same_keys(input_scheme, dict_to_normalize)
