"""
appendixa base module.

This is the principal module of the appendixa project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""
import Polygon
import random

# example constant variable
NAME = "appendixa"


class Segment:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.polygon = None

    def number_of_exits(self):
        floor_space = self.polygon.area()
        selection = random.randrange(1,20,1)

        if selection in range(1, 3):
            if floor_space < 600:
                return 1
            else:
                return 2
        elif selection in range(4, 6):
            if floor_space < 600:
                return 2
            else:
                return 3
        elif selection in range(7, 9):
            if floor_space < 600:
                return 3
            else:
                return 4
        elif selection in range(10, 12):
            if floor_space < 1200:
                return 0
            else:
                return 1
        elif selection in range(13, 15):
            if floor_space < 1600:
                return 0
            else:
                return 1
        elif selection in range(16, 18):
            return random.randrange(1,4,1)
        else:
            return 1
    
    def exit_location(self, current_heading):
        selection = random.randrange(1,20,1)

        if selection in range(1, 7):
            return current_heading
        elif selection in range(8, 12):
            return (current_heading + 90) % 360
        elif selection in range(13, 17):
            return (current_heading - 90) % 360
        else:
            return (current_heading + 180) % 360
    
class Room(Segment):
    def __init__(self, x, y, rotation=0) -> None:
        super().__init__(x, y)
        self.polygon = Polygon.Polygon(((x, y), (x, y+30), (x+30, y+30), (x+30, y)))
        self.polygon.rotate(rotation)

    def has_exits(self):
        return True

class AddRoom:
    def __init__(self, x, y, rotation=0) -> None:
        self.x = x
        self.y = y
        
    def execute(self, generation_queue, segments, current_heading):
        new_room = Room(self.x, self.y)
        exits = new_room.number_of_exits()
        print(f'There are {exits} exits in the room')
        segments.append(new_room)

        for exit in range(exits):
            exit_location = new_room.exit_location(current_heading)
            print(f'Exit location is {exit_location}')


            generation_queue.append(AddExit(new_room.x, new_room.y)
