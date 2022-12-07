import math as m

def a_square(base: float) -> float:
    """
    Calculates the area of a square
    :param base:
    :return m.pow(base, 2):
    """
    area = m.pow(base, 2)
    area = float(area)
    return area

def a_rectangle(width: float, height: float) -> float:
    """
    Calculates area of a rectangle
    :param width:
    :param height:
    :return width * height:
    """
    area = width * height
    area = float(area)
    return area

def a_triangle(width: float, height: float) -> float:
    """
    Calculates area of a triangle
    :param width:
    :param height:
    :return (width * height)/2:
    """
    area = (width * height)/2
    area = float(area)
    return area

def a_circle(radius):
    """
    Calculates area of a circle
    :param radius:
    :return m.pi * m.pow(radius, 2):
    """
    area = m.pi * m.pow(radius, 2)
    area = float(area)
    return area