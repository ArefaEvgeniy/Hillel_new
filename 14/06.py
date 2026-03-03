def func(a, b, c):
    try:
        print("Start function")
        x = (a + b[1]) / c
        print(x)
    # except ZeroDivisionError:
    #     print("Error: Division by zero is not allowed.")
    #     x = 0
    except IndexError:
        print("Error: List index out of range.")
        x = 10
    except LookupError:
        print("Error: Lookup Error.")
        x = -10
    except ValueError:
        print("Error: Invalid value.")
        x = 20

    print("Finish function")
    return x


q = 100
w = [35, 56, 45]
e = 0

print("START")
try:
    result = func(q, w, e)
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
    result = 100

print(f"result = {result}")
print("END")
