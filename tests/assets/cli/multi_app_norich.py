import doctyper

sub_app = doctyper.Typer()

variable = "Some text"


@sub_app.command()
def hello(
    name: str = "World", age: int = doctyper.Option(0, help="The age of the user")
):
    """
    Say Hello
    """


@sub_app.command()
def hi(user: str = doctyper.Argument("World", help="The name of the user to greet")):
    """
    Say Hi
    """


@sub_app.command()
def bye():
    """
    Say bye
    """


app = doctyper.Typer(help="Demo App", epilog="The end", rich_markup_mode=None)
app.add_typer(sub_app, name="sub")


@app.command()
def top():
    """
    Top command
    """
