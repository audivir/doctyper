import doctyper


def main(
    id: int = doctyper.Argument(..., min=0, max=1000),
    age: int = doctyper.Option(20, min=18),
    score: float = doctyper.Option(0, max=100),
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    doctyper.run(main)
