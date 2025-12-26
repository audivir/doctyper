from enum import Enum

import doctyper


class Food(str, Enum):
    food_1 = "Eggs"
    food_2 = "Bacon"
    food_3 = "Cheese"


app = doctyper.Typer()


@app.command()
def main(groceries: list[Food] = doctyper.Option([Food.food_1, Food.food_3])):
    print(f"Buying groceries: {', '.join([f.value for f in groceries])}")


if __name__ == "__main__":
    app()
