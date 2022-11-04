import json
import typer
from src.index import normalizeit


def main(input_schema: str,  output_schema: str):
    normalizeit()
    
if __name__ ==  "__main__":
    typer.run(main)

