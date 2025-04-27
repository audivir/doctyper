from typing import Optional

import doctyper


def name_callback(ctx: doctyper.Context, value: str):
    if ctx.resilient_parsing:
        return
    print("Validating name")
    if value != "Camila":
        raise doctyper.BadParameter("Only Camila is allowed")
    return value


def main(name: Optional[str] = doctyper.Option(default=None, callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
