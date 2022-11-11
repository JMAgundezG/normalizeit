"""First defined normalization strategy."""

from .normalization_strategy import NormalizationStrategy
from ..utils.json_utils import same_keys


class NormalizeItNormalizationStrategy(NormalizationStrategy):
    """
    First defined normalization strategy.
    """

    def fetch_data(self, input_scheme: dict, dict_to_fetch: dict) -> dict:
        data = {}
        for key, value in input_scheme.keys():
            if self.config.value_id_str in key:
                data[key] = dict_to_fetch[key]
            if isinstance(value, dict):
                data.update(self.fetch_data(value, dict_to_fetch[key]))
        return data

    def normalize_func(
        self, input_scheme: dict, output_scheme: dict, dict_to_normalize: dict
    ) -> dict:
        pass

    def validate_dict_to_normalize(
        self, input_scheme: dict, dict_to_normalize: dict
    ) -> bool:
        """This needs a lot more of validation"""
        return same_keys(input_scheme, dict_to_normalize)
