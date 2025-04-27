from typing import Optional

import doctyper
from typing_extensions import Annotated


def main(
    accept: Annotated[Optional[bool], doctyper.Option("--accept/--reject")] = None,
):
    if accept is None:
        print("I don't know what you want yet")
    elif accept:
        print("Accepting!")
    else:
        print("Rejecting!")


if __name__ == "__main__":
    doctyper.run(main)
