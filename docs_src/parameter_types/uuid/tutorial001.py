from uuid import UUID

import doctyper


def main(user_id: UUID):
    print(f"USER_ID is {user_id}")
    print(f"UUID version is: {user_id.version}")


if __name__ == "__main__":
    doctyper.run(main)
