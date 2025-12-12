import doctyper

app = doctyper.Typer()


@app.command()
def main(name: str = doctyper.Argument("World", envvar=["AWESOME_NAME", "GOD_NAME"])):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    app()
