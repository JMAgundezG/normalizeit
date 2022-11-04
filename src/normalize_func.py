from utils.json_utils import same_keys

def validate_dict_to_normalize(input_scheme: dict, dict_to_normalize: dict) -> bool:
    """ This needs a lot more of validation """
    return same_keys(input_scheme, dict_to_normalize)

def fetch_data(input_scheme: dict, dict_to_normalize: dict) -> dict:
    data = {}
    for key, value in input_scheme:
        if type(value) is not dict:
            if "$$" in value:
                data[value] == dict_to_normalize[key]
        else:
            data.update(fetch_data(value, dict_to_normalize[key]))
    return data


def normalize_func(input_scheme: dict, output_scheme: dict, dict_to_normalize: dict) -> dict:
    if not validate_dict_to_normalize(input_scheme, dict_to_normalize):
        raise Exception("[ERROR] input JSON cannost be validated with the selected input scheme")
    
    return {}