def func(x):
    return x ** 2 if x % 2 else x ** 3


squared_numbers_2 = [func(x) for x in range(1, 6)]
print(squared_numbers_2)


squared_numbers = [(lambda x: x**2 if x % 2 else x ** 3)(x) for x in range(1, 6)]
print(squared_numbers)
