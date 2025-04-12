"""modul do obliczen geometrycznych 3d"""


def cube_volume(edge_length):
    """returns the volume of a cube with given edge length"""
    return edge_length ** 3


def cube_area(edge_length):
    """returns the area of a cube with given edge length"""
    return 6 * edge_length ** 2


def rectangular_cuboid_volume(edge_length1, edge_length2, edge_length3):
    """returns the volume of a rectangular cuboid with given edges"""
    return edge_length1 * edge_length2 * edge_length3


def rectangular_cuboid_area(edge_length1, edge_length2, edge_length3):
    """returns the area of a rectangular cuboid with given edges"""
    return 2 * (edge_length1 * edge_length2 + edge_length1 * edge_length3 + edge_length2 * edge_length3)


def ball_volume(radius):
    """returns the volume of a ball with given radius"""
    return 4 / 3 * 3.14 * radius ** 3


def ball_area(radius):
    """returns the area of a ball with given radius"""
    return 4 * 3.14 * radius ** 2
