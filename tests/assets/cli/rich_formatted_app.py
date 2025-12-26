from typing import Annotated

import doctyper

app = doctyper.Typer(
    rich_markup_mode="rich",
)


@app.command(help="Say [bold red]hello[/bold red] to the user.")
def hello(
    user_1: Annotated[
        str,
        doctyper.Argument(help="The [bold]cool[/bold] name of the [green]user[/green]"),
    ],
    user_2: Annotated[str, doctyper.Argument(help="The world")] = "The World",
    force: Annotated[
        bool, doctyper.Option(help="Force the welcome [red]message[/red]")
    ] = False,
):
    print(f"Hello {user_1} and {user_2}")  # pragma: no cover


if __name__ == "__main__":
    app()
