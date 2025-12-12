import doctyper

app = doctyper.Typer()


@app.command()
def main(name: str = doctyper.Argument("World", hidden=True)):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
