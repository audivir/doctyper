import doctyper

app = doctyper.Typer()


@app.command()
def main(name: str = doctyper.Argument()):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
