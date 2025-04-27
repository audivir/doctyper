from typing import List

import doctyper


def main(number: List[float] = doctyper.Option([])):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    doctyper.run(main)
