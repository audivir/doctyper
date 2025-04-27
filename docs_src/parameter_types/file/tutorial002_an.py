import doctyper
from typing_extensions import Annotated


def main(config: Annotated[doctyper.FileTextWrite, doctyper.Option()]):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    doctyper.run(main)
