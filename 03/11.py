a = [12, 15, 20, "hello", 25.5, True, None]
b = []
c = [0,]
d = list()

print(type(a))
print(a)
print(b)
print(c)
print(d)

print(len(a))
print(20 in a)
print(21 in a)
print(a[0])
print(a[3])
print(a[6])
print(a[-1])
print(a[4])
# print(a[7])

if len(a) > 5:
    print(a[5])
