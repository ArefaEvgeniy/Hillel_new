class Woman:

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight + 10 if self.__weight < 50 else \
            (self.__weight * 0.75 if self.__weight > 70 else self.__weight)


woman_1 = Woman("Anna", 25, 100)
print(f"name: {woman_1.name}")
print(f"age: {woman_1._age}")
print(f"weight: {woman_1._Woman__weight}")

print(woman_1.get_weight())
