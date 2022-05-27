city = "São Paulo"

print(city.encode("utf_8"))

print(city.encode("utf_16"))

print(city.encode("iso8859_1"))


try:
    print(city.encode("cp437"))

except UnicodeEncodeError as error:
    print(error)

print(city.encode("cp437", errors="ignore"))

print(city.encode("cp437", errors="replace"))

print(city.encode("cp437", errors="xmlcharrefreplace"))
