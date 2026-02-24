class Auto(object):

    def __init__(self, wells, motor, name, color, speed):
        self.wells = wells
        self.motor = motor
        self.name = name
        self.color = color
        self.speed = speed

    def move(self):
        print(f"The car {self.name}-{self.color} is driving")

    def stop(self):
        print("This car is stopping")

    def turn(self, direction="left"):
        print(f"This car is turning {direction}")


my_car = Auto(4, "V8", "Mustang", "red", 0)
my_car_2 = Auto(4, "V8", "Mustang", "blue", 0)

print(my_car.__dict__)
print(my_car_2.__dict__)

my_car.move()
my_car_2.move()
