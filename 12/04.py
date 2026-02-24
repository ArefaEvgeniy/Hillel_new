class Auto(object):

    def __init__(self, wells=4, motor="V8", name="Mustang", color="red", speed=0):
        self.wells = wells
        self.motor = motor
        self.name = name
        self.color = color
        self.speed = speed

    def move(self):
        print(f"The car {self.name}-{self.color} is driving")
        self.speed += 10

    def stop(self):
        print("This car is stopping")
        self.speed = 0

    def turn(self, direction="left"):
        print(f"This car is turning {direction}")
        self.speed -= 5
        print(f"speed after turn: {self.speed}")
        self.move()


my_car = Auto()
my_car_2 = Auto(color="blue")

print(my_car.__dict__)
print(my_car_2.__dict__)

my_car.move()
my_car.move()
my_car.move()
my_car_2.move()
print(f"speed of my_car: {my_car.speed}")
print(f"speed of my_car_2: {my_car_2.speed}")

print("------------------")
my_car.stop()
print(f"speed of my_car: {my_car.speed}")
print(f"speed of my_car_2: {my_car_2.speed}")

print("------------------")
my_car_2.turn()
print(f"speed of my_car: {my_car.speed}")
print(f"speed of my_car_2: {my_car_2.speed}")
