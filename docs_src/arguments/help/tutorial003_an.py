import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(name: Annotated[str, doctyper.Argument(help="Who to greet")] = "World"):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
