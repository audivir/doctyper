import doctyper

app = doctyper.Typer()


@app.command()
def delete(name: str):
    print(f"Deleting user: {name}")
