from typing import Annotated

import doctyper


def main(name: Annotated[str, doctyper.Argument()]):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
