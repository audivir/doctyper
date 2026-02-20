import doctyper

app = doctyper.Typer(suggest_commands=True)


@app.command()
def create():
    doctyper.echo("Creating...")


@app.command()
def delete():
    doctyper.echo("Deleting...")


if __name__ == "__main__":
    app()
