import doctyper
from typing_extensions import Annotated


def main(
    name: Annotated[
        str, doctyper.Argument(envvar="AWESOME_NAME", show_envvar=False)
    ] = "World",
):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    doctyper.run(main)
