human = {"name": "Alexander",
        "lastname": "Glock",
        "age": 36,
        "address": {"street": "Lisova", "house": 87, "flat": [1, 3, 7, 9]}
}

print(human["address"]["flat"][0])
print(human["address"]["flat"][-1])

lastname = human.pop("lastname")
print(lastname)

print(human)
