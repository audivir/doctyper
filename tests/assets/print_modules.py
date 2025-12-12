import sys

import doctyper

app = doctyper.Typer()


@app.command()
def main():
    for m in sys.modules:
        print(m)


if __name__ == "__main__":
    app()
