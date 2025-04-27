import doctyper
from typing_extensions import Annotated


def main(name: Annotated[str, doctyper.Argument()] = "Wade Wilson"):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
