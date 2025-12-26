import doctyper

app = doctyper.Typer()


@app.command()
def main(name: str = doctyper.Argument(..., help="The name of the user to greet")):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
