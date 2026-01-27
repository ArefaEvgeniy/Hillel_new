lst = [4, 6, 8, -11, 7, 45, -10, 32, 21, -5550, 90, 11, 23, 42]

sum = 0
negative_indexes = []
# index = 0
for index, number in enumerate(lst):
    if number < 0:
        negative_indexes.append(index)
        # index += 1
        continue
    if number % 2 == 0:
        sum += number
    # index += 1
else:
    print("Else")

print("Sum of even numbers:", sum)
print("Indexes of negative numbers:", negative_indexes)

for data in enumerate(lst):
    print(data)
