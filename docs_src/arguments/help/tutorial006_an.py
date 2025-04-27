import doctyper
from typing_extensions import Annotated


def main(name: Annotated[str, doctyper.Argument(metavar="✨username✨")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
