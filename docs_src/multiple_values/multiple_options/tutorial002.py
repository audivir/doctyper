from typing import List

import doctyper

app = doctyper.Typer()


@app.command()
def main(number: List[float] = doctyper.Option([])):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    app()
