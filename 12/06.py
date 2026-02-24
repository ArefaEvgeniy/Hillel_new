class Auto:
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


class Truck(Auto):
    def __init__(self, wells=6, motor="V12", name="MAN", color="white", speed=0, load_capacity=12000):
        super().__init__(wells, motor, name, color, speed)
        self.load_capacity = load_capacity

    def turn(self, direction="left"):
        print(f"This car is turning {direction}")
        self.speed -= 7
        print(f"speed after turn: {self.speed}")
        self.move()


truck = Truck()
print(truck.__dict__)
truck.move()
truck.turn()
truck.stop()
