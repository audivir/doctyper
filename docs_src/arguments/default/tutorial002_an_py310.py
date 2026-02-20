import random
from typing import Annotated

import doctyper

app = doctyper.Typer()


def get_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


@app.command()
def main(name: Annotated[str, doctyper.Argument(default_factory=get_name)]):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
