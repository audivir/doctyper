from typing import List

import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(
    name: Annotated[List[str], doctyper.Option(help="The name to say hi to.")] = [
        "World"
    ],
):
    for each_name in name:
        print(f"Hello {each_name}")


if __name__ == "__main__":
    app()
