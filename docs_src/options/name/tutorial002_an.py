import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(user_name: Annotated[str, doctyper.Option("--name", "-n")]):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    app()
