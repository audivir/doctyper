import doctyper
from typing_extensions import Annotated


def main(
    name: Annotated[str, doctyper.Argument(help="Who to greet")],
    lastname: Annotated[
        str,
        doctyper.Argument(help="The last name", rich_help_panel="Secondary Arguments"),
    ] = "",
    age: Annotated[
        str,
        doctyper.Argument(help="The user's age", rich_help_panel="Secondary Arguments"),
    ] = "",
):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
