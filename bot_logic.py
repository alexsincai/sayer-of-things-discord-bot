from file_handler import read_from_file, write_to_file
from random import choice


def parse(text):
    args = [x.strip() for x in text.lower().split(" ")]
    command = args[0]

    if command == "ping":
        return "pong"

    if command == "quote":
        quotes = read_from_file()

        if len(args) > 1 and args[1] is not None:
            quotes = [q for q in quotes if q["author"] == args[1]]

        return choice(quotes)["quote"]

    if command == "remember":
        if len(args) > 2:
            name = args[1]
            string = " ".join(*[args[2:]])

            if len(name) and len(string):
                write_to_file(name, string)

            return f"I'll remembere that dep quote by **{name}**"

    return
