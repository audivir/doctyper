from typing import Literal

import doctyper

app = doctyper.Typer()


@app.command()
def main(network: Literal["simple", "conv", "lstm"] = doctyper.Option("simple")):
    print(f"Training neural network of type: {network}")


if __name__ == "__main__":
    app()
