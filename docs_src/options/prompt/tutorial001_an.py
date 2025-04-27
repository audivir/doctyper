import doctyper
from typing_extensions import Annotated


def main(name: str, lastname: Annotated[str, doctyper.Option(prompt=True)]):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    doctyper.run(main)
