import json
import pickle


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


class Pilot(Human):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number

    def __str__(self):
        return f"{super().__str__()} They have a pilot's license number {self.license_number}."


class Stuart(Human):
    def __init__(self, name, age, airline):
        super().__init__(name, age)
        self.airline = airline

    def __str__(self):
        return f"{super().__str__()} They work for {self.airline}."


class Airplane:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity
        self.crew = []

    def __str__(self):
        return f"The airplane model is {self.model} with a capacity of {self.capacity} passengers."

    def add_crew_member(self, crew_member):
        self.crew.append(crew_member)

    def remove_crew_member(self, crew_member):
        self.crew.remove(crew_member)

    def info(self):
        crew_info = "\n".join(str(member) for member in self.crew)
        return f"{self}\nCrew Members:\n{crew_info}"


if __name__ == "__main__":
    pilot = Pilot("John Doe", 35, "P12345")
    stuart_1 = Stuart("Jane Smith", 28, "Airline XYZ")
    stuart_2 = Stuart("Emily Davis", 30, "Airline ABC")
    airplane = Airplane("Boeing 737", 180)
    # airplane.add_crew_member(pilot)
    # airplane.add_crew_member(stuart_1)
    # airplane.add_crew_member(stuart_2)

    # print(airplane.info())

    objects = [pilot, stuart_1, stuart_2, airplane]

    data = []
    for item in (objects):
        if item.__class__.__name__ == "Pilot":
            data.append({
                "type": "Pilot",
                "name": item.name,
                "age": item.age,
                "license_number": item.license_number
            })
        elif item.__class__.__name__ == "Stuart":
            data.append({
                "type": "Stuart",
                "name": item.name,
                "age": item.age,
                "airline": item.airline
            })
        elif item.__class__.__name__ == "Airplane":
            data.append({
                "type": "Airplane",
                "model": item.model,
                "capacity": item.capacity
            })

    print(data)
    with open("data_air.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

    airplane.add_crew_member(pilot)
    airplane.add_crew_member(stuart_1)
    airplane.add_crew_member(stuart_2)
    with open("data_air.pkl", "wb") as file:
        pickle.dump(objects, file)

import datetime
