import doctyper
from typing_extensions import Annotated


def main(verbose: Annotated[int, doctyper.Option("--verbose", "-v", count=True)] = 0):
    print(f"Verbose level is {verbose}")


if __name__ == "__main__":
    doctyper.run(main)
