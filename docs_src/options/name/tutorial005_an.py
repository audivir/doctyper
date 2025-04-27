import doctyper
from typing_extensions import Annotated


def main(
    name: Annotated[str, doctyper.Option("--name", "-n")],
    formal: Annotated[bool, doctyper.Option("--formal", "-f")] = False,
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
