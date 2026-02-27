class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def distance_from_origin(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


if __name__ == "__main__":
    point_1 = Point(1, 2)
    point_2 = Point(1, 4)
    point_3 = Point(1, 2)

    print(point_1.x)
    print(point_1.y)
    print(point_1)
    print(point_2)

    print(point_1 != point_2)
    print(point_1 != point_3)

    point_4 = point_1 + point_2
    print(point_4)
    print(point_4.distance_from_origin())
