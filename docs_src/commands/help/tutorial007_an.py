from typing import Union

import doctyper
from typing_extensions import Annotated

app = doctyper.Typer(rich_markup_mode="rich")


@app.command()
def create(
    username: Annotated[str, doctyper.Argument(help="The username to create")],
    lastname: Annotated[
        str,
        doctyper.Argument(
            help="The last name of the new user", rich_help_panel="Secondary Arguments"
        ),
    ] = "",
    force: Annotated[
        bool, doctyper.Option(help="Force the creation of the user")
    ] = False,
    age: Annotated[
        Union[int, None],
        doctyper.Option(
            help="The age of the new user", rich_help_panel="Additional Data"
        ),
    ] = None,
    favorite_color: Annotated[
        Union[str, None],
        doctyper.Option(
            help="The favorite color of the new user",
            rich_help_panel="Additional Data",
        ),
    ] = None,
):
    """
    [green]Create[/green] a new user. :sparkles:
    """
    print(f"Creating user: {username}")


@app.command(rich_help_panel="Utils and Configs")
def config(configuration: str):
    """
    [blue]Configure[/blue] the system. :gear:
    """
    print(f"Configuring the system with: {configuration}")


if __name__ == "__main__":
    app()
