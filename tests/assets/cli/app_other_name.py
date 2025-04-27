import doctyper

application = doctyper.Typer()


@application.command()
def callback(name: str = "World"):
    doctyper.echo(f"Hello {name}")
