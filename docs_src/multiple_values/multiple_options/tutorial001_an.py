from typing import List, Optional

import doctyper
from typing_extensions import Annotated


def main(user: Annotated[Optional[List[str]], doctyper.Option()] = None):
    if not user:
        print(f"No provided users (raw input = {user})")
        raise doctyper.Abort()
    for u in user:
        print(f"Processing user: {u}")


if __name__ == "__main__":
    doctyper.run(main)
