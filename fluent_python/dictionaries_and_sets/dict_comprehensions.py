dial_codes = [
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
]

country_dial = {country: code for code, country in dial_codes}

print(country_dial)

print({
    code: country.upper()
    for country, code in sorted(country_dial.items()) if code < 70})


# unpacking mappings
def dump(**kwargs):
    return kwargs


print(dump(**{"x": 1}, y=2, **{"z": 3}))


# merging mappings with |
d1 = {"a": 1, "b": 3}
d2 = {"a": 2, "b": 4, "z": 3}

print(d1 | d2)


# pattern matching with mappings
def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        case {"type": "book"}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")


b1 = dict(api=1, author="Douglas Hofstadter", type="book", title="Godel, Escher, Bach")

print(get_creators(b1))
