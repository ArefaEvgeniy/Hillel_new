def func(x):
    def inner_func(y):
        return x + y * 2

    return inner_func


new_func = func(5)
print(new_func(10))
