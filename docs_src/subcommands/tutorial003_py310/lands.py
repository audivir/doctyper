import doctyper

import reigns
import towns

app = doctyper.Typer()
app.add_typer(reigns.app, name="reigns")
app.add_typer(towns.app, name="towns")

if __name__ == "__main__":
    app()
