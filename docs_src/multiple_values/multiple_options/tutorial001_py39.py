from typing import Optional

import doctyper

app = doctyper.Typer()


@app.command()
def main(user: Optional[list[str]] = doctyper.Option(None)):
    if not user:
        print(f"No provided users (raw input = {user})")
        raise doctyper.Abort()
    for u in user:
        print(f"Processing user: {u}")


if __name__ == "__main__":
    app()
