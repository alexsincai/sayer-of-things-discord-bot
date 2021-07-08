HEADERS = ["author", "quote"]


def read_from_file():
    from csv import DictReader

    with open("quotes.csv", "r") as file:
        return [r for r in DictReader(f=file, fieldnames=HEADERS)]


def write_to_file(name, text):
    from csv import DictWriter

    current = ensure_uniq([*read_from_file(), {"author": name, "quote": text}][1:])

    with open("quotes.csv", "w") as file:
        writer = DictWriter(
            f=file,
            fieldnames=HEADERS,
        )
        writer.writeheader()

        for line in current:
            writer.writerow(line)


def ensure_uniq(array):
    ret = []
    for line in array:
        if line not in ret:
            ret.append(line)
    return ret
