import doctyper

app = doctyper.Typer()


@app.command()
def main(config: doctyper.FileTextWrite = doctyper.Option(...)):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    app()
