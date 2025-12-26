from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(number: Annotated[list[float], doctyper.Option()] = []):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    app()
