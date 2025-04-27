from typing import Optional

import doctyper
from typing_extensions import Annotated

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise doctyper.Exit()


def name_callback(name: str):
    if name != "Camila":
        raise doctyper.BadParameter("Only Camila is allowed")
    return name


def main(
    name: Annotated[str, doctyper.Option(callback=name_callback)],
    version: Annotated[
        Optional[bool],
        doctyper.Option("--version", callback=version_callback, is_eager=True),
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
