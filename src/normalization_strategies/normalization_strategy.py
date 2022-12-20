""" This is something that I should resolve """


from src.config.config import ConfigSingleton


class NormalizationStrategy:
    """
    First defined normalization strategy.
    """

    def __init__(self):
        """Constructor"""
        self.config = ConfigSingleton()

    def fetch_data(self, dict_to_fetch: dict) -> dict:
        """
        Fetches data from a dict using the input scheme from config file
        """

    def normalize(self, dict_to_normalize: dict) -> dict:
        """
        Method that normalizes a dict using with the format of output_scheme
        """

    def validate_dict_to_normalize(
        self, dict_to_normalize: dict
    ) -> bool:
        """This needs a lot more of validation"""