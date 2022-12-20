class FetchStrategy:
    """
    Definition of the fetching data strategy.
    """

    def __init__(self):
        """Constructor"""

    def fetch_data(
        self, dict_to_fetch: dict, fetch_schema: dict, identifier: str
    ) -> dict:
        """
        Fetches data from a dict using the input scheme from config file
        """
        raise NotImplementedError

    def validate(self, input_scheme: dict, dict_to_normalize: dict) -> bool:
        """
        Validate if the dict to normalize can be fetched using the input scheme
        """
        raise NotImplementedError
