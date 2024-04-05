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
from appendixa.vector import Vector
from appendixa.room import Room
from appendixa.segment import Segment

# example constant variable
NAME = "appendixa"

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class AddRoom:
    def __init__(self, x, y, rotation=0) -> None:
        self.x = x
        self.y = y
        
    def execute(self, generation_queue, segments, current_heading):
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
        

            #generation_queue.append(AddExit(new_room.x, new_room.y)
