a = [1, 22, -5, 0, 34, 7, -22, 8]

b = {x[0]: x[1] ** 2 for x in enumerate(a)}
print(b)

a = {1: 0, '3': "three", '3': "34", '3': 0, "e": 0, "pi": [3.14, "tt"]}
print(a)

import string

print(string.ascii_letters)
first = 'a'
second = 'A'
print(ord(first))
print(ord(second))

