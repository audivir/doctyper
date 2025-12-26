from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(user_name: Annotated[str, doctyper.Option("--name")]):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    app()
