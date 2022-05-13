symbols = "$%£^&"
codes = [ord(symbol) for symbol in symbols]
print(codes)

print("*** Local scope ***")
codes = [last := ord(c) for c in symbols]
print(last)