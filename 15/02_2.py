import json

from air_02 import Pilot, Stuart, Airplane


with open("data_air.json", "r", encoding="utf-8") as file:
    data = json.load(file)

objects = []
for item in data:
    if item["type"] == "Pilot":
        objects.append(Pilot(item["name"], item["age"], item["license_number"]))
    elif item["type"] == "Stuart":
        objects.append(Stuart(item["name"], item["age"], item["airline"]))
    elif item["type"] == "Airplane":
        objects.append(Airplane(item["model"], item["capacity"]))

for obj in objects:
    print("-------------------")
    print(obj)
    print(type(obj))

print(objects[0].name)
print(objects[0].age)
