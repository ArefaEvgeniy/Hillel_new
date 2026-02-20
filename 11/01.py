text = "Hello, world! Прівит!\nSecond line.\nThird line.\n    Last line    "

file = open("viktoria.txt", "w", encoding="utf-8")
file.write(text)
file.close()

try:
    file_2 = open("viktoria.txt", "r", encoding="utf-8")
    content = file_2.read()
finally:
    file_2.close()

print(content)
print("------------------")

with open("viktoria.txt", "r", encoding="utf-8") as file_3:
    content_2 = file_3.read(6)
    content_3 = file_3.read(5)
    print(content_2)
    print(content_3)
    print("------------------")

with open("viktoria.txt", "r", encoding="utf-8") as file_4:
    content_1 = file_4.readline().strip()
    content_2 = file_4.readline().strip()
    content_3 = file_4.readline().strip()
    content_4 = file_4.readline().strip()
    print(content_1)
    print(content_2)
    print(content_3)
    print(content_4)
    print("------------------")

with open("viktoria.txt", encoding="utf-8") as file_4:
    content = file_4.readlines()
    print(content)
