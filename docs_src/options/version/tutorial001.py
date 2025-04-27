from typing import Optional

import doctyper

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise doctyper.Exit()


def main(
    name: str = doctyper.Option("World"),
    version: Optional[bool] = doctyper.Option(
        None, "--version", callback=version_callback
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
