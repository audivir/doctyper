import click
import doctyper

app = doctyper.Typer()


def shell_complete(ctx: click.Context, param: click.Parameter, incomplete: str):
    doctyper.echo(f"ctx: {ctx.info_name}", err=True)
    doctyper.echo(f"arg is: {param.name}", err=True)
    doctyper.echo(f"incomplete is: {incomplete}", err=True)
    return ["Emma"]


@app.command(context_settings={"auto_envvar_prefix": "TEST"})
def main(name: str = doctyper.Argument(shell_complete=shell_complete)):
    """
    Say hello.
    """


if __name__ == "__main__":
    app()
