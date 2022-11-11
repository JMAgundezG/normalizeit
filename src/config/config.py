"""
    Created by @JMAgundezG 5/11/2022
"""
from typing import Optional
import json


class SingletonMeta(type):
    "SingletonMeta type"
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigSingleton(metaclass=SingletonMeta):
    """
    Class to save all the configuration needed in the project
    """

    input_scheme: dict = {}
    output_scheme: dict = {}

    input_scheme_path: str = ""
    output_scheme_path: str = ""

    value_id_str: str = "$$"

    def __init__(
        self,
        input_scheme_path: str = "./input_scheme.json",
        output_scheme_path: str = "./output_scheme.json",
        value_id_str: str = "$$",
    ):
        self.input_scheme_path = input_scheme_path
        self.output_scheme_path = output_scheme_path
        self.input_scheme: dict = self.load_scheme_file(
            input_scheme_path, "input scheme file"
        )
        self.output_scheme: dict = self.load_scheme_file(
            output_scheme_path, "output scheme file"
        )

        if not self.is_valid_id(value_id_str):
            raise Exception(f"[ERROR] ID [{value_id_str}] is not valid")
        self.value_id_str = value_id_str

    @staticmethod
    def is_valid_id(identificator):
        """Check if the value id has a good identificator"""
        return len(identificator) and all(not c.isalnum() for c in identificator)

    @staticmethod
    def load_scheme_file(scheme_path: str, error_message: Optional[str] = "") -> dict:
        """Load an scheme file using the path"""
        try:
            with open(scheme_path, "r", encoding="utf-8") as scheme_file:
                return json.loads(scheme_file.read())
        except Exception as exc:
            raise Exception(f"[ERROR] {error_message} not found") from exc

    def __str__(self):
        return (
            f"<ConfigSingleton> [input_scheme_path:{self.input_scheme_path}]"
            f" [output_scheme_path:{self.output_scheme_path}]"
            f" [value_id_str:'{self.value_id_str}']"
        )
