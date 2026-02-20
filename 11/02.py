with open("viktoria.txt", "rb") as file:
    content = file.read()

print(content)
print("------------------")
# print(content.decode("Windows-1251"))

with open("viktoria.txt", "rb") as file:
    content = file.read(21)
    print(content)
    print("------------------")

print(content.decode())
