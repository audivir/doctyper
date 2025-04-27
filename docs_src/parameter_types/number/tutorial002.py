import doctyper


def main(
    id: int = doctyper.Argument(..., min=0, max=1000),
    rank: int = doctyper.Option(0, max=10, clamp=True),
    score: float = doctyper.Option(0, min=0, max=100, clamp=True),
):
    print(f"ID is {id}")
    print(f"--rank is {rank}")
    print(f"--score is {score}")


if __name__ == "__main__":
    doctyper.run(main)
