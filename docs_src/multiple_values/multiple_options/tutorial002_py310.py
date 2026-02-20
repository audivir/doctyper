import doctyper

app = doctyper.Typer()


@app.command()
def main(number: list[float] = doctyper.Option([])):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    app()
