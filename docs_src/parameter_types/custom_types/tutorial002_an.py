import click
import doctyper
from typing_extensions import Annotated


class CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"<CustomClass: value={self.value}>"


class CustomClassParser(click.ParamType):
    name = "CustomClass"

    def convert(self, value, param, ctx):
        return CustomClass(value * 3)


app = doctyper.Typer()


@app.command()
def main(
    custom_arg: Annotated[
        CustomClass, doctyper.Argument(click_type=CustomClassParser())
    ],
    custom_opt: Annotated[
        CustomClass, doctyper.Option(click_type=CustomClassParser())
    ] = "Foo",
):
    print(f"custom_arg is {custom_arg}")
    print(f"--custom-opt is {custom_opt}")


if __name__ == "__main__":
    app()
