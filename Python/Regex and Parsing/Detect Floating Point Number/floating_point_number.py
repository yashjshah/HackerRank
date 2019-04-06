import re

for _ in range(int(input())):
    line = input()
    line_is_float = bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',line))
    print(line_is_float)
