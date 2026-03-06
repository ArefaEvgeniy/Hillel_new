import json


with open("data.json", "r", encoding="utf-8") as file:
    data = file.read()

print(type(data))
print(data)
print(data[:10])


with open("data.json", "r", encoding="utf-8") as file:
    data_2 = json.load(file)

print(type(data_2))
print(data_2)
print(data_2[0])
