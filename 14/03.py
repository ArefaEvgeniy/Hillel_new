class MyStr(str):
    def __sub__(self, other):
        return self.replace(other, "", 1)


a = MyStr("Hello, World!")
b = MyStr("World")
c = MyStr("Viktoria")
print(a)
print(a.upper())
print(a * 5)

print(a - b)
print(a - c)
