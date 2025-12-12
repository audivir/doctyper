import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(
    name: Annotated[
        str,
        doctyper.Argument(
            help="Who to greet", show_default="Deadpoolio the amazing's name"
        ),
    ] = "Wade Wilson",
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
