set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set3 = set1.union(set2)
set31 = set1 | set2
print(set3)
print(set31)

set4 = set1.intersection(set2)
set41 = set1 & set2
print(set4)
print(set41)

set5 = set1.difference(set2)
set51 = set1 - set2
print(set5)
print(set51)

for item in set1:
    print(item)
