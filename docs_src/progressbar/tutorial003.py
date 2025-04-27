import time

import doctyper


def main():
    total = 0
    with doctyper.progressbar(range(100)) as progress:
        for value in progress:
            # Fake processing time
            time.sleep(0.01)
            total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    doctyper.run(main)
