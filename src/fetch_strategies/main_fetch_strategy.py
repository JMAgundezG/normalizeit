from src.utils.json_utils import same_keys

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
        for key, value in fetch_schema.items():
            if identifier in value and key in dict_to_fetch.keys():
                data[value] = dict_to_fetch[key]
            if isinstance(value, dict):
                data.update(self.fetch_data(dict_to_fetch[key], value, identifier))
        return data

    def validate(self, input_scheme: dict, dict_to_normalize: dict) -> bool:
        return same_keys(input_scheme, dict_to_normalize)
