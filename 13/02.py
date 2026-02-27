from task_01 import Point


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_radius = self.radius + other.radius
            return Circle(new_x, new_y, new_radius)
        return NotImplemented


circle_1 = Circle(5, 2, 3)
print(circle_1)
print(circle_1.distance_from_origin())

circle_2 = Circle(1, 7, 2)
circle_3 = circle_1 + circle_2
print(circle_3)
print(circle_3 + "Hello")
