"""
appendixa base module.

This is the principal module of the appendixa project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""
import Polygon, Polygon.Utils
import random
import math
from .room import *
from .passage import *

# example constant variable
NAME = "appendixa"

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class AddExit:
    def __init__(self, x, y, wall_normal) -> None:
        self.x = x
        self.y = y
        self.normal_vector = wall_normal

    def execute(self, generation_queue, segments, current_heading):
        
        projected_vector = self.normal_vector*0
        x = self.x + projected_vector.x
        y = self.y + projected_vector.y

        if self.normal_vector.x == 0:
            if self.normal_vector.y > 0:
                x -= 5
            else:
                x += 5
        else:
            if self.normal_vector.x > 0:
                y += 5
            else:
                y -= 5

        print(f'Adding passage at {x}, {y} with rotation {Vector.angle(self.normal_vector)}')
        new_passage = Passage(x, y, Vector.angle(self.normal_vector)-math.radians(90))
        segments.append(new_passage)


class AddRoom:
    def __init__(self, x, y, rotation=0) -> None:
        self.x = x
        self.y = y
        
    def execute(self, generation_queue, segments, current_heading):
        print(f'Adding room at {self.x}, {self.y}')

        new_room = Room(self.x, self.y)
        exits = new_room.number_of_exits()
        print(f'There are {exits} exits in the room')
        segments.append(new_room)

        exit_locations = { 'left': 0, 'right': 0, 'opposite': 0, 'same': 0 }
        for exit in range(exits):
            exit_location = new_room.exit_location(current_heading)
            exit_locations[exit_location] += 1
            print(f'Exit location is {exit_location}')

            wall_segment = new_room.select_wall_segment(exit_location, current_heading)
            print(f'Wall segment is {wall_segment}')

            # find the normalized vector of the wall edge
            wall_vector = Vector(wall_segment[1][0] - wall_segment[0][0], wall_segment[1][1] - wall_segment[0][1])
            wall_normal = wall_vector.PerpendicularCounterClockwise().getNormalised()

            print (f'Wall vector is {wall_vector}')
            print (f'Wall normal is {wall_normal}')

            midpoint = ((wall_segment[0][0] + wall_segment[1][0]) / 2, (wall_segment[0][1] + wall_segment[1][1]) / 2)
            print(f'Midpoint of wall edge is {midpoint}')

            rotation_angle = Vector.angle(wall_normal) - math.radians(90)
            print(f'Angle of wall normal is {rotation_angle} radians or {math.degrees(rotation_angle)} degrees')
            generation_queue.append(AddExit(midpoint[0], midpoint[1], wall_normal))
