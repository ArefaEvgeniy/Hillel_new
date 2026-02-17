def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result

    return wrapper


@decorator
def func_1():
    print("This is function 1.")


@decorator
def func_2(x, y):
    return x + y


func_1()
print("-" * 20)
print(func_2(5, 10))
