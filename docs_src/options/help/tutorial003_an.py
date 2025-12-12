import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(fullname: Annotated[str, doctyper.Option(show_default=False)] = "Wade Wilson"):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    app()
