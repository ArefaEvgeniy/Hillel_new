import json


data = [
    {
        "name": "John",
        "age": 35,
        "surname": "Doe",
        "occupation": "Pilot"
    },
    {
        "name": "Jane",
        "age": 28,
        "surname": "Smith",
        "occupation": "Stuart",
        "family": None
    },
    {
        "name": "Emily",
        "age": 30,
        "surname": "Davis",
        "occupation": ("Stuart", "Pilot"),
        "children": ["Alice", "Bob"]
    }
]

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

print(data[0])
print(data[0].get("name"))
