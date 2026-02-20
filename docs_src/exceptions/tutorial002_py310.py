import doctyper

app = doctyper.Typer(pretty_exceptions_show_locals=True)


@app.command()
def main(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app()
