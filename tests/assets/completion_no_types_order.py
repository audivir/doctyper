import doctyper

app = doctyper.Typer()


def complete(args, incomplete, ctx):
    doctyper.echo(f"info name is: {ctx.info_name}", err=True)
    doctyper.echo(f"args is: {args}", err=True)
    doctyper.echo(f"incomplete is: {incomplete}", err=True)
    return [
        ("Camila", "The reader of books."),
        ("Carlos", "The writer of scripts."),
        ("Sebastian", "The type hints guy."),
    ]


@app.command()
def main(name: str = doctyper.Option("World", autocompletion=complete)):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
