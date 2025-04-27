import doctyper

app = doctyper.Typer()


@app.command()
def version():
    print("My CLI Version 1.0")
