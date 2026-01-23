a = [12, 15, 20, "hello", [1, 0, "RRR", [6, 67]], 25.5]

print(len(a))

print(1 in a)
print(1 in a[4])
print(6 in a[4][3])
print(a[4][2])
print(a[4][3][-1])

a.append("New Item")
a.append(999)
print(a)
a.insert(1, "Inserted Item")
print(a)
a[1] = 0
print(a)

del a[0]
print(a)
a.remove("hello")
print(a)

if "hello" in a:
    a.remove("hello")

b = a.pop()
c = a.pop()
a.pop()
print(a)
print(b)
print(c)
dd = a.pop(0)
print(a)
