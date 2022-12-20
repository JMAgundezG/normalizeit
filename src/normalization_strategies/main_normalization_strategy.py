"""First defined normalization strategy."""

from copy import deepcopy

from src.fetch_strategies.main_fetch_strategy import MainFetchStrategy
from src.output_strategies.main_output_strategy import MainOutputStrategy

from ..utils.json_utils import same_keys
from .normalization_strategy import NormalizationStrategy


class MainNormalizationStrategy(NormalizationStrategy):
    """
    First defined normalization strategy.
    """

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.fetch_strategy = MainFetchStrategy()
        self.output_strategy = MainOutputStrategy()

    def fetch_data(self, dict_to_fetch: dict) -> dict:
        """
        Fetches data from a dict using the input scheme from config file
        """
        return self.fetch_strategy.fetch_data(
            dict_to_fetch, self.config.input_scheme, self.config.identifier
        )

    def normalize(self, dict_to_normalize: dict) -> dict:
        data = self.fetch_data(dict_to_normalize)
        return self.create_normalized_dict(data)

    def create_normalized_dict(self, data: dict) -> dict:
        return self.output_strategy.write_output(
            data, deepcopy(self.config.output_scheme)
        )

    def validate_dict_to_normalize(
        self, dict_to_normalize: dict
    ) -> bool:
        """This needs a lot more of validation"""
        return self.fetch_strategy.validate(input_scheme=self.config.input_scheme, dict_to_normalize=dict_to_normalize)
