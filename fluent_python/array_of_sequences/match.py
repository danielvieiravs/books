
class InvalidCommand(Exception):
    pass


metro_areas = [
    ("Tokyo", "JP", 36.933, (35432.3121, 5435.1212)),
    ("London", "UK", 40.1234, (-1254786.3121, -21553.1212)),
]

for metro in metro_areas:

    match metro:

        case [name, _, _, (lat, lon)] if lon <= 0:
           print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")

        case ["Tokyo", "JP", _, (lat, lon)]:
            print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")

        case _:
            raise InvalidCommand(metro)
