import math as m

def a_square(base):
    area = m.pow(base, 2)
    area = float(area)
    return area

def a_rectangle(width, height):
    area = width * height
    area = float(area)
    return area

def a_triangle(width, height):
    area = (width * height)/2
    area = float(area)
    return area

def a_circle(radius):
    area = m.pi * m.pow(radius, 2)
    area = float(area)
    return area