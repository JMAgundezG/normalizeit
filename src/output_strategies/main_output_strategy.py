"""Main output strategy class."""

from copy import deepcopy

from src.output_strategies.output_strategy import OutputStrategy


class MainOutputStrategy(OutputStrategy):
    """Main output strategy class."""

    def write_output(self, normalized_data: dict, output_scheme: dict):
        """Write the output using the output scheme"""
        normalized_dict = deepcopy(output_scheme)
        for key, value in output_scheme.items():
            if isinstance(value, dict):
                normalized_dict[key] = self.write_output(
                    normalized_data, normalized_dict[key]
                )
            else:
                if value in normalized_data.keys():
                    normalized_dict[key] = normalized_data[value]
        return normalized_dict
