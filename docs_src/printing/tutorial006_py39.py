import doctyper

app = doctyper.Typer()


@app.command()
def main(name: str):
    doctyper.secho(f"Welcome here {name}", fg=doctyper.colors.MAGENTA)


if __name__ == "__main__":
    app()
