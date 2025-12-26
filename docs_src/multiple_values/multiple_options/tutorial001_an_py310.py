from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(user: Annotated[list[str] | None, doctyper.Option()] = None):
    if not user:
        print(f"No provided users (raw input = {user})")
        raise doctyper.Abort()
    for u in user:
        print(f"Processing user: {u}")


if __name__ == "__main__":
    app()
