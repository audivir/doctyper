import doctyper

doctyper.main.HAS_RICH = False

app = doctyper.Typer()


@app.command()
def main(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app()
