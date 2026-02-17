a = [3, 45, 667, '34', '0', -3, 445, 0, -1000]


def func(x):
    if not isinstance(x, int):
        return 0
    elif x > 0:
        return x ** 2
    return abs(x)


new_a = list(map(func, a))
print(new_a)

new_a_2 = list(map(lambda x: 0 if not isinstance(x, int) else x ** 2 if x > 0 else abs(x), a))
print(new_a_2)
