from typing import Optional

import doctyper
from typing_extensions import Annotated


def name_callback(value: str):
    if value != "Camila":
        raise doctyper.BadParameter("Only Camila is allowed")
    return value


def main(
    name: Annotated[Optional[str], doctyper.Option(callback=name_callback)] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
