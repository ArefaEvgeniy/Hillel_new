a = 0


if a > 50:
    print("a is large positive")
    if a >= 100:
        print("a is very large positive")
    elif a == 0:
        print("a is zero")
elif a > 0:
    print("a is positive")
elif a < 0:
    print("a is negative")
