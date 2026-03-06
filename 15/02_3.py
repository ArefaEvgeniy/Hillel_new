import pickle


with open("data_air.pkl", "rb") as file:
    objects = pickle.load(file)

for obj in objects:
    print("-------------------")
    print(obj)
    print(type(obj))

print("-------------------")
print(objects[-1].info())
