from enum import Enum
from typing import Annotated

import doctyper


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


app = doctyper.Typer()


@app.command()
def main(
    network: Annotated[
        NeuralNetwork, doctyper.Option(case_sensitive=False)
    ] = NeuralNetwork.simple,
):
    print(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    app()
