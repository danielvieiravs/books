import collections
import re
import sys

from types import MappingProxyType
from typing import Type


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


food = dict(category="ice cream", flavor="vanilla", cost=199)

match food:
    case {"category": "ice cream", **details}:
        print(f"Ice Cream details: {details}")


# defaultdict
WORD_RE = re.compile(r"\w+")

index = collections.defaultdict(list)
with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


# chainmap
d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

chain = collections.ChainMap(d1, d2)

print(chain["a"])
print(chain["c"])


# counter
counter = collections.Counter("abracadabra")

print(counter)

print(counter.update("aaaaazzz"))

print(counter.most_common(3))


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


# immutable mappings
d = {1: "A"}

d_proxy = MappingProxyType(d)

print(d_proxy)

print(d_proxy[1])

try:
    d_proxy[2] = "X"
except TypeError:
    d[2] = "B"

print(d_proxy)

# dictionary views
d = dict(a=10, b=20, c=30)

values = d.values()

print(values)

print(len(values))

print(list(values))

print(reversed(values))

try:
    print(values[0])
except TypeError as error:
    print(error)

d["z"] = 99

print(d)

print(values)
