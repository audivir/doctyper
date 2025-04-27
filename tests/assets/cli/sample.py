import doctyper

app = doctyper.Typer()


@app.command()
def hello(name: str = "World", formal: bool = False):
    """
    Say hi
    """
    if formal:
        doctyper.echo(f"Good morning Ms. {name}")
    else:
        doctyper.echo(f"Hello {name}!")


@app.command()
def bye(friend: bool = False):
    """
    Say bye
    """
    if friend:
        doctyper.echo("Goodbye my friend")
    else:
        doctyper.echo("Goodbye")
