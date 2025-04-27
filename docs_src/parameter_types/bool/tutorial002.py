from typing import Optional

import doctyper


def main(accept: Optional[bool] = doctyper.Option(None, "--accept/--reject")):
    if accept is None:
        print("I don't know what you want yet")
    elif accept:
        print("Accepting!")
    else:
        print("Rejecting!")


if __name__ == "__main__":
    doctyper.run(main)
