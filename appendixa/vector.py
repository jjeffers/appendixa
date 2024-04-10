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
    
    @classmethod
    def midpoint(cls, point1, point2):
        return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
    
    @classmethod
    def angle(cls, vector):
        return math.atan2(vector.y, vector.x)
    
    def PerpendicularClockwise(self):
        return Vector(self.y, -self.x)
    
    def PerpendicularCounterClockwise(self):
        return Vector(-self.y, self.x)
    


    