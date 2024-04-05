import math
from vector2d import Vector2D

class Vector(Vector2D):
    typecode = 'f'

    def __init__(self, x, y):
        super().__init__(x, y)

    @classmethod
    def from_angle(cls, angle_in_degrees):
        angle = math.radians(angle_in_degrees)

        return cls(
            round(math.cos(angle),0), 
            round(math.sin(angle),0))


    