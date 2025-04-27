import doctyper
from typing_extensions import Annotated


def main(
    fullname: Annotated[
        str, doctyper.Option(show_default="Deadpoolio the amazing's name")
    ] = "Wade Wilson",
):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    doctyper.run(main)
