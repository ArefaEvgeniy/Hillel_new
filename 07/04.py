set1 = {1, 2, 3, 4, 5}
set2 = frozenset({45, 677, 24, 0})
set3 = {45, 677, 24, 0}

print(set1)
print(set2)

set1.add(set2)

print(set1)

