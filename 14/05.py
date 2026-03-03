a = 100
b = [35, 56, 45]
c = 0

# if c != 0:
try:
    print("START")
    x = (a + b[1]) / c
    print(x)
# except ZeroDivisionError:
#     x = 0
except (IndexError, LookupError, ValueError):
    x = 10
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#     x = 100
else:
    print("No exceptions were raised.")
finally:
    print("Finally block executed.")

print(f"x = {x}")
print("END")
