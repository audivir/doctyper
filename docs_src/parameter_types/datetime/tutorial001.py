from datetime import datetime

import doctyper

app = doctyper.Typer()


@app.command()
def main(birth: datetime):
    print(f"Interesting day to be born: {birth}")
    print(f"Birth hour: {birth.hour}")


if __name__ == "__main__":
    app()
