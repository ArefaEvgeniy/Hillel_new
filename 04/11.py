lst = [4, 6, 8, -11, 7, 45, -10, 32, 21, -5550, 90, 11, 23, 42]
i = 0
sum = 0
while i < len(lst):
    if lst[i] % 2 == 0:
        sum = sum + lst[i]
    i += 1

print("Sum of even numbers:", sum)


sum = 0
for number in lst:
    if number < 0:
        continue
    if number == 11:
        break
    if number % 2 == 0:
        sum += number
else:
    print("Else")

print("Sum of even numbers:", sum)
