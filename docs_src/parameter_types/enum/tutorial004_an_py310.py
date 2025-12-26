from typing import Annotated, Literal

import doctyper

app = doctyper.Typer()


@app.command()
def main(
    network: Annotated[Literal["simple", "conv", "lstm"], doctyper.Option()] = "simple",
):
    print(f"Training neural network of type: {network}")


if __name__ == "__main__":
    app()
