def calculate_area(length: float, width: float = 0) -> str:
    """
    Calculate the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    area = f"Area: {length * width}"
    return area


print(calculate_area(5, 3))
print(calculate_area(5))
print(calculate_area.__annotations__)
