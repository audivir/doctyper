import doctyper
from typing_extensions import Annotated

valid_names = ["Camila", "Carlos", "Sebastian"]


def complete_name(incomplete: str):
    completion = []
    for name in valid_names:
        if name.startswith(incomplete):
            completion.append(name)
    return completion


app = doctyper.Typer()


@app.command()
def main(
    name: Annotated[
        str,
        doctyper.Option(help="The name to say hi to.", autocompletion=complete_name),
    ] = "World",
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
