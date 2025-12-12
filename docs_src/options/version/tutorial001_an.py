from typing import Optional

import doctyper
from typing_extensions import Annotated

__version__ = "0.1.0"

app = doctyper.Typer()


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise doctyper.Exit()


@app.command()
def main(
    name: Annotated[str, doctyper.Option()] = "World",
    version: Annotated[
        Optional[bool], doctyper.Option("--version", callback=version_callback)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
