import doctyper
from typing_extensions import Annotated


def main(
    id: Annotated[int, doctyper.Argument(min=0, max=1000)],
    age: Annotated[int, doctyper.Option(min=18)] = 20,
    score: Annotated[float, doctyper.Option(max=100)] = 0,
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    doctyper.run(main)
