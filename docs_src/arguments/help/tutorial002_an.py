import doctyper
from typing_extensions import Annotated


def main(
    name: Annotated[str, doctyper.Argument(help="The name of the user to greet")],
):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
