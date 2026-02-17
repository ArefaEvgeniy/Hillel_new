def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@decorator
def along_function():
    print("This is a long function that does many things.")


# along_function()

# along_function = decorator(along_function)
along_function()
