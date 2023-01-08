"""
Created by @JMAgundezG 11/11/2022
Main file os normalizeIt project"""

from typing import Optional

from src.config.config import Config
from src.normalization_strategies.main_normalization_strategy import \
    MainNormalizationStrategy


class NormalizeIt:
    """Main object of the project"""

    def __init__(
        self,
        input_scheme: dict = None,
        output_scheme: dict = None,
        value_id_str: Optional[str] = "$$",
    ):
        args = {
            "input_scheme": input_scheme,
            "output_scheme": output_scheme,
        }
        if value_id_str:
            args["value_id_str"] = value_id_str
        self.config = Config(**args)

    def normalize(self, dict_to_normalize: dict) -> dict:
        """
        Normalize the dict passed using the configuration already loaded
        """
        return MainNormalizationStrategy(self.config).normalize(dict_to_normalize)

    def validate(self, dict_to_validate: dict) -> bool:
        """Validate dict using configuration"""
        return MainNormalizationStrategy(self.config).validate_dict_to_normalize(
            dict_to_validate
        )
