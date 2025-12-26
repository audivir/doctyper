from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(
    name: str,
    lastname: Annotated[
        str, doctyper.Option(help="Last name of person to greet.")
    ] = "",
    formal: Annotated[
        bool,
        doctyper.Option(
            help="Say hi formally.", rich_help_panel="Customization and Utils"
        ),
    ] = False,
    debug: Annotated[
        bool,
        doctyper.Option(
            help="Enable debugging.", rich_help_panel="Customization and Utils"
        ),
    ] = False,
):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    app()
