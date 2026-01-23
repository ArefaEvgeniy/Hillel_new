a = [12, 15, 20, "hello", 67, 25.5, 44, "world", 0, None]

b = a[1:4]
c = a[:]
print(b)
print(a[1:2])
print(a[0:7])
print(a[5:])
print(a[0:])
print(c)
print(id(a))
print(id(c))
print(a[1:-1])
print(a[1:-1:1])
print(a[1:-1:2])
print(a[::3])
print(a[7:0:-2])
print(a[-1::-1])
print(a[::-1])
