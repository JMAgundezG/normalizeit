import json

import typer


def main(input_schema: str, output_schema: str, json_to_normalize: str, variable_identificator: Optional[str] = typer.Argument(None)):
    normalizeit(input_schema, output_schema, json_to_normalize, variable_identificator)


if __name__ == "__main__":
    typer.run(main)
