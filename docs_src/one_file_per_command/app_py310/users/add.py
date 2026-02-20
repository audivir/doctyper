import doctyper

app = doctyper.Typer()


@app.command()
def add(name: str):
    print(f"Adding user: {name}")
