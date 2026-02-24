class Auto():

    def move(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopping")

    def turn(self, direction="left"):
        print(f"This car is turning {direction}")


my_car = Auto()
my_car.wells = 4
my_car.motor = "V8"
my_car.name = "Mustang"
my_car.color = "red"
my_car. speed = 0

my_car_2 = Auto()
my_car_2.wells = 4
my_car_2.motor = "V8"
my_car_2.name = "Mustang"
my_car_2.color = "blue"
my_car_2. speed = 0

print(my_car.__dict__)
print(my_car_2.__dict__)
