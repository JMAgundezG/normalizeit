class OutputStrategy(object):
    def __init__(self):
        pass

    def write_output(self, normalized_data: dict, output_scheme: dict):
        raise NotImplementedError
