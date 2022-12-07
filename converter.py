import math as m
from calculate import *

def inches_to_feet(area: float) -> float:
    calc = area / 12
    return calc

def inches_to_yards(area: float) -> float:
    calc = area / 36
    return calc

def inches_to_miles(area: float) -> float:
    calc =  area / 63360
    return calc

def feet_to_inches(area: float) -> float:
    calc = area * 12
    return calc

def feet_to_yards(area: float) -> float:
    calc = area / 3
    return calc

def feet_to_miles(area: float) -> float:
    calc = area / 5280
    return calc

def yards_to_inches(area: float) -> float:
    calc = area * 36
    return calc

def yards_to_feet(area: float) -> float:
    calc = area * 3
    return calc

def yards_to_miles(area: float) -> float:
    calc = area / 1760
    return calc

def miles_to_inches(area: float) -> float:
    calc = area * 63360
    return calc

def miles_to_feet(area: float) -> float:
    calc = area * 5280
    return calc

def miles_to_yards(area: float) -> float:
    calc = area * 1760
    return calc







