from copy import deepcopy

from output_strategies.output_strategy import OutputStrategy


class MainOutputStrategy(OutputStrategy):
    def write_output(self, normalized_data: dict, output_scheme: dict):
        print("normalized_data", normalized_data, "output_scheme", output_scheme)
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
