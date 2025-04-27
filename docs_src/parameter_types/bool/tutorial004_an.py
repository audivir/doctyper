import doctyper
from typing_extensions import Annotated


def main(in_prod: Annotated[bool, doctyper.Option(" /--demo", " /-d")] = True):
    if in_prod:
        print("Running in production")
    else:
        print("Running demo")


if __name__ == "__main__":
    doctyper.run(main)
