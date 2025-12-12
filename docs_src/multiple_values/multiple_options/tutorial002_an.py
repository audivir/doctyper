from typing import List

import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(number: Annotated[List[float], doctyper.Option()] = []):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    app()
