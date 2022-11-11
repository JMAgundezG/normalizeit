""" This is something that I should resolve """


from src.config.config import ConfigSingleton


class NormalizationStrategy:
    """
    First defined normalization strategy.
    """

    def __init__(self):
        """Constructor"""
        self.config = ConfigSingleton()

    def fetch_data(self, input_scheme: dict, dict_to_fetch: dict) -> dict:
        """
        Method that fetches the data from a dict using the variables name of input_scheme
        """

    def normalize_func(
        self, input_scheme: dict, output_scheme: dict, dict_to_normalize: dict
    ) -> dict:
        """
        Method that normalizes a dict using with the format of output_scheme
        """
