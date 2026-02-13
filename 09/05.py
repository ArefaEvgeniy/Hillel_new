def square(x):
    return x ** 2


square_2 = lambda x: x ** 2

print(square(5))  # Виведе 25
print(square_2(5))  # Виведе 25


def super_func(x, y):
    if x > y:
        return x - y
    elif x == 0:
        return y ** 2
    else:
        return x * y


super_func_2 = lambda x, y: x - y if x > y else (y ** 2 if x == 0 else x * y)

print(super_func(10, 5))  # Виведе 5
print(super_func(3, 4))   # Виведе 12
print(super_func_2(10, 5))  # Виведе 5
print(super_func_2(3, 4))   # Виведе 12
