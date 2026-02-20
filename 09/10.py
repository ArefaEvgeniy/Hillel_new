def func_1(n):
    while n > 0:
        return n
        n -= 1


def func_2(n):
    while n > 0:
        yield n
        n -= 1


def func_3(n):
    while True:
        yield n
        n -= 2


print(func_1(5))
print(func_1(5))
print(func_1(5))

print("------------------")
my_generator = func_2(5)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

print("start for loop")
for item in my_generator:
    print(item)

print("------------------")
my_generator_3 = func_3(5)
for item in my_generator_3:
    print(item)
