n = 1
while n <= 10:
    if n % 3 == 0:
        n = n + 1
        continue
    print(n)
    n = n + 1

print('End')

n = 0
while n < 10:
    n = n + 1
    if n % 3 == 0:
        continue
    print(n)

print('End')

n = 1
while n <= 10:
    if n % 3 != 0:
        print(n)
    n = n + 1

print('End')
