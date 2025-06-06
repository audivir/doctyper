import time

import doctyper


def iterate_user_ids():
    # Let's imagine this is a web API, not a range()
    for i in range(100):
        yield i


def main():
    total = 0
    with doctyper.progressbar(iterate_user_ids(), length=100) as progress:
        for value in progress:
            # Fake processing time
            time.sleep(0.01)
            total += 1
    print(f"Processed {total} user IDs.")


if __name__ == "__main__":
    doctyper.run(main)
