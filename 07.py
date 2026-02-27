class Car:
    doors = 4


class Truck(Car):
    weels = 6

    def __init__(self, number, color):
        self.number = number
        self.color = color


truck_1 = Truck("AA0000AA", "white")
truck_2 = Truck("BB0000BB", "black")
truck_3 = Truck("CC0000CC", "red")

truck_3.weels = 8
print(truck_3.weels)
print(truck_1.weels)
Truck.weels = 10
print(truck_1.weels)
print(truck_2.weels)
print(truck_3.weels)
print(truck_3.doors)
