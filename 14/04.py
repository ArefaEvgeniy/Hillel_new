a = 100
b = [35, 56, 45]
c = 10

# if c != 0:
try:
    print("START")
    x = (a + b[1]) / c
    print(x)
    if x < 20:
        raise ValueError("x is less than 20")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    x = 0
except IndexError:
    print("Error: List index out of range.")
    x = 10
except LookupError:
    print("Error: Lookup Error.")
    x = -10
except ValueError:
    print("Error: Invalid value.")
    x = 20
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    x = 100

print(f"x = {x}")
print("END")
