import doctyper

sub_app = doctyper.Typer()


@sub_app.command()
def hello():
    doctyper.echo("sub hello")


@sub_app.command()
def bye():
    doctyper.echo("sub bye")


cli = doctyper.Typer()
cli.add_typer(sub_app, name="sub")


@cli.command()
def top():
    doctyper.echo("top")
