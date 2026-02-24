# class Auto(object):
class Auto():
    wells = 4
    motor = "V8"
    name = "Mustang"
    color = "red"
    speed = 0

    def move(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopping")

    def turn(self, direction="left"):
        print(f"This car is turning {direction}")


my_car = Auto()
my_car_2 = Auto()
my_car.move()
my_car.stop()
print(my_car.name)
print(my_car.color)
my_car.turn()
my_car.turn("right")
my_car.turn(direction="backwards")

print("------------------")
print(my_car.color)
print(my_car_2.color)
my_car_2.color = "blue"
print("------------------")
print(my_car.color)
print(my_car_2.color)
my_car_2.sits = 2
print(my_car_2.sits)
# print(my_car.sits)
print(my_car.__dict__)
print(my_car_2.__dict__)

print(my_car.wells)
print(my_car_2.wells)
print("------------------")
Auto.wells = 6
print(my_car.wells)
print(my_car_2.wells)

print("------------------")
Auto.color = "black"
print(my_car.color)
print(my_car_2.color)
