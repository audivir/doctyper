import doctyper
from typing_extensions import Annotated


def main(name: Annotated[str, doctyper.Argument(hidden=True)] = "World"):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
