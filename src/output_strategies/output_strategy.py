"""Base class for output strategies."""


class OutputStrategy:
    """Base class for output strategies."""

    def __init__(self):
        """Constructor"""

    def write_output(self, normalized_data: dict, output_scheme: dict):
        """Write the output using the output scheme"""
        raise NotImplementedError
