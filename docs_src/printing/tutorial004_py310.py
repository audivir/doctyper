import doctyper
from rich.console import Console

err_console = Console(stderr=True)

app = doctyper.Typer()


@app.command()
def main():
    err_console.print("Here is something written to standard error")


if __name__ == "__main__":
    app()
