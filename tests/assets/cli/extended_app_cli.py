import doctyper

sub_sub_app = doctyper.Typer()


@sub_sub_app.command()
def sub_sub_command():
    doctyper.echo("sub_sub_command")


sub_app = doctyper.Typer()
sub_app.add_typer(sub_sub_app, name="sub")


@sub_app.command()
def hello():
    doctyper.echo("hello there")


@sub_app.command()
def bye():
    doctyper.echo("bye bye")


cli = doctyper.Typer()
cli.add_typer(sub_app)


@cli.command()
def top():
    doctyper.echo("top")
