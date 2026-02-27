class Car:
    numbers_of_objects = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.count_objects()

    @classmethod
    def count_objects(cls):
        cls.numbers_of_objects += 1


class Truck(Car):
    numbers_of_objects = 0

    def __init__(self, name, color, load_capacity):
        super().__init__(name, color)
        self.load_capacity = load_capacity


print(Car.numbers_of_objects)
car_1 = Car("Mustang", "red")
print(Car.numbers_of_objects)
car_2 = Car("Camaro", "yellow")
car_3 = Car("Challenger", "black")
print(car_2.numbers_of_objects)

print("------------------")
truck_1 = Truck("MAN", "white", 12000)
truck_2 = Truck("Scania", "blue", 15000)
print(Truck.numbers_of_objects)
print(Car.numbers_of_objects)
