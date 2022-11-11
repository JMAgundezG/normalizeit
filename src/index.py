"""
Created by @JMAgundezG 11/11/2022
Main file os normalizeIt project"""

from typing import Optional
from src.config.config import ConfigSingleton


class NormalizeIt:
    """Main object of the project"""

    def __init__(
        self,
        input_scheme_path: str,
        output_scheme_path: str,
        value_id_str: Optional[str],
    ):
        args = {
            "input_scheme_path": input_scheme_path,
            "output_scheme_path": output_scheme_path,
        }
        if value_id_str:
            args["value_id_str"] = value_id_str
        ConfigSingleton(**args)

    def normalize(self, dict_to_normalize: dict) -> dict:
        """
            Normalize the dict passed using the configuration already loaded
        """
        return dict_to_normalize

    def validate(self, dict_to_validate: dict) -> bool:
        """ Validate dict using configuration """
        return dict_to_validate
