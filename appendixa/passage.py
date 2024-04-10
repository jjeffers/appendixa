from .segment import Segment
import Polygon, Polygon.Utils
from appendixa.vector import Vector
import random

class Passage(Segment):
    def __init__(self, x, y, rotation_angle) -> None:
        super().__init__(x, y)
        self.polygon = Polygon.Polygon(((x, y), (x, y+30), (x+10, y+30), (x+10, y)))
        self.polygon.rotate(rotation_angle, x, y)