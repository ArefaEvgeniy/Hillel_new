a = [3, 45, 667, '34', '0', -3, 445, 0, -1000]


def func(x):
    if isinstance(x, int) and x > 0:
        return x * 2
    else:
        return x


new_a = list(filter(func, a))
print(new_a)

new_a_2 = list(filter(lambda x: isinstance(x, int) and x > 0, a))
print(new_a_2)
