def func():
    return "Hello, World!"


print(func())
print(func)

a = func
del func

print(a())
