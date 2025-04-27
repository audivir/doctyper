import doctyper

cli = doctyper.Typer()
sub_app = doctyper.Typer()
cli.add_typer(sub_app)


@sub_app.command()
def hello():
    doctyper.echo("hello there")


@sub_app.command()
def bye():
    doctyper.echo("bye bye")
