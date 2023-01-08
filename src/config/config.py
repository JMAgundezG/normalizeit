"""
    Created by @JMAgundezG 5/11/2022
"""
from typing import Optional


class Config:
    """
    Class to save all the configuration needed in the project
    """

    def __init__(
        self,
        input_scheme: Optional[dict] = None,
        output_scheme: Optional[dict] = None,
        value_id_str: str = "$$",
    ):
        self.input_scheme: dict = input_scheme
        self.output_scheme: dict = output_scheme

        if not self.is_valid_id(value_id_str):
            raise Exception(f"[ERROR] ID [{value_id_str}] is not valid")
        self.value_id_str = value_id_str

    @staticmethod
    def is_valid_id(identificator):
        """Check if the value id has a good identificator"""
        return len(identificator) and all(not c.isalnum() for c in identificator)

    def __str__(self):
        return (
            f"<ConfigSingleton> [input_scheme:{self.input_scheme}]"
            f" [output_scheme:{self.output_scheme}]"
            f" [value_id_str:'{self.value_id_str}']"
        )
