import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(config: Annotated[doctyper.FileText, doctyper.Option(mode="a")]):
    config.write("This is a single line\n")
    print("Config line written")


if __name__ == "__main__":
    app()
