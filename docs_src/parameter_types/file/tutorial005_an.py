import doctyper
from typing_extensions import Annotated


def main(config: Annotated[doctyper.FileText, doctyper.Option(mode="a")]):
    config.write("This is a single line\n")
    print("Config line written")


if __name__ == "__main__":
    doctyper.run(main)
