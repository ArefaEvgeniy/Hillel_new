t = (1, "hello", [3, 4, 5])

print(id(t))
t[2].append(6)
print(t)
print(id(t))

a = [1,]
b = [1]

print(a == b)
print(a)
print(b)

c = (1,)
d = (1)

print(c == d)
print(c)
print(d)
