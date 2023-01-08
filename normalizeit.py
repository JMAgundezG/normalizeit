from typing import Optional

import typer

from src.index import NormalizeIt
from src.utils.json_utils import json_to_dict
from src.utils.loader import load_scheme_file

app = typer.Typer()


def parse_data(
    input_scheme_path: str,
    output_scheme_path: str,
    input_scheme: str,
    output_scheme: str,
):

    """Parse data from cli"""
    clean_input_scheme = (
        json_to_dict(input_scheme)
        if True
        else load_scheme_file(input_scheme_path, "input scheme file")
        if output_scheme_path
        else None
    )
    clean_output_scheme = (
        json_to_dict(output_scheme)
        if output_scheme
        else load_scheme_file(output_scheme_path, "output scheme file")
        if output_scheme_path
        else None
    )
    return clean_input_scheme, clean_output_scheme


@app.command()
def normalize(
    data: str,
    input_scheme_path: str = None,
    output_scheme_path: str = None,
    input_scheme: str = None,
    output_scheme: str = None,
    value_id_str: Optional[str] = None,
):
    """Normalize a dict using a input and output scheme"""

    clean_input_scheme, clean_output_scheme = parse_data(
        input_scheme_path, output_scheme_path, input_scheme, output_scheme
    )
    if not all([clean_input_scheme, clean_output_scheme]):
        raise Exception(
            "You must provide an input scheme and an output scheme to normalize a dict"
        )
    normalize_it = NormalizeIt(clean_input_scheme, clean_output_scheme, value_id_str)
    dict_json = json_to_dict(data)

    print(normalize_it.normalize(dict_json))


@app.command()
def validate(
    input_scheme_path: str = None,
    input_scheme: str = None,
    data: str = None,
):
    clean_input_scheme = parse_data(input_scheme_path, None, input_scheme, None)[0]

    if not clean_input_scheme:
        raise Exception("You must provide an input scheme to validate a dict")
    normalize_it = NormalizeIt(clean_input_scheme, None)
    print(normalize_it.validate(json_to_dict(data)))


if __name__ == "__main__":
    app()
