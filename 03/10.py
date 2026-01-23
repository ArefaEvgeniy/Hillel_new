a = -10

if a > 0:
    print("a is positive")
else:
    print("a is non-positive")

print("a is positive") if a > 0 else print("a is non-positive")

if a > 0:
    c = 100
else:
    c = -100

c = 100 if a > 0 else -100
print(c)

if a > 0:
    print("a is positive")
elif a == 0:
    print("a is zero")
else:
    print("a is non-positive")

print("a is positive") if a > 0 else (print("a is zero") if a == 0 else print("a is non-positive"))
