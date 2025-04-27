import doctyper

app = doctyper.Typer()


@app.command()
def main(name: str = "morty"):
    print(name)


broken_app = doctyper.Typer()


@broken_app.command()
def broken(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app(standalone_mode=False)

    doctyper.main.get_command(broken_app)()
