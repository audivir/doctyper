import time

import doctyper


def main():
    total = 1000
    with doctyper.progressbar(length=total) as progress:
        for batch in range(4):
            # Fake processing time
            time.sleep(1)
            # Increment by 250 on each loop iteration
            # (it will take 4 seconds to reach 1000)
            progress.update(250)
    print(f"Processed {total} things in batches.")


if __name__ == "__main__":
    doctyper.run(main)
