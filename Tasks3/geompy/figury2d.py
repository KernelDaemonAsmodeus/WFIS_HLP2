"""modul do obliczen geometrycznych 2d"""


def square_area(side_length):
    """returns area of a square"""
    return side_length ** 2


def square_perimeter(side_length):
    """returns perimeter of a square"""
    return side_length * 4


def rectangle_area(side_length1, side_length2):
    """calculates area of a rectangle"""
    return side_length1 * side_length2


def rectangle_perimeter(side_length1, side_length2):
    """calculates perimeter of a rectangle"""
    return side_length1 * 2 + side_length2 * 2


def circle_area(radius):
    """returns area of a circle"""
    return 3.14 * radius ** 2


def circle_circumference(radius):
    """returns circumference of a circle"""
    return 2 * 3.14 * radius
