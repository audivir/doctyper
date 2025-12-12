import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(name: str, lastname: Annotated[str, doctyper.Option(prompt=True)]):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    app()
