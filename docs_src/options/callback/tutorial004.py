from typing import Optional

import doctyper

app = doctyper.Typer()


def name_callback(ctx: doctyper.Context, param: doctyper.CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    print(f"Validating param: {param.name}")
    if value != "Camila":
        raise doctyper.BadParameter("Only Camila is allowed")
    return value


@app.command()
def main(name: Optional[str] = doctyper.Option(default=None, callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
