a = {1: "one", '3': "three", "e": 56, "pi": [3.14, "tt"], 0: "zero", "er": "AAA", 2: "two", (1, 2): "tuple_key"}

print(len(a))
print(a["e"])
print(a["pi"])
print(a[2])
print(a[0])
print(a["er"])
print(a['3'])

print(a)

print(a.keys())
print(a.values())
print(a.items())

print("-" * 50)
for item in a:
    print(a[item])

print("-" * 50)
for item in a.values():
    print(item)

print("-" * 50)
for key in a:
    print(f"Key: {key}, Value: {a[key]}")

print("-" * 50)
for item in a.items():
    print(f"Key: {item[0]}, Value: {item[-1]}")

print("-" * 50)
for key, value in a.items():
    print(f"Key: {key}, Value: {value}")

a.update({"Inna": "programmer"})

if "Inna" in a:
    print(a["Inna"])
else:
    print("No such key")

print(a.get("Alisa", "No such key"))
print(a.get("Inna", "No such key"))

a.update({"Inna": "cooker"})
print(a["Inna"])

a["Inna"] = "driver"
print(a["Inna"])

a.pop("Inna")
print(a)

print(a[(1, 2)])
