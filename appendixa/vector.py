import math
from vector2d import Vector2D

class Vector(Vector2D):
    typecode = 'f'

    def __init__(self, x, y):
        super().__init__(x, y)

    def __init__(self, angle_in_degrees, radius=1):
        angle = math.radians(angle_in_degrees)
        print(angle)
        super().__init__(
            round(radius*math.cos(angle),0), 
            round(radius*math.sin(angle),0))


    