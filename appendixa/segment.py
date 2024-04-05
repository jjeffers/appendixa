import random
import Polygon, Polygon.Utils

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
            return 'opposite'
        elif selection in range(8, 12):
            return 'right'
        elif selection in range(13, 17):
            return 'left'
        else:
            return 'same'
        
    def direction_from_heading(self, location, current_heading):
        selection = random.randrange(1,20,1)

        if location == 'opposite':
            return current_heading
        elif location == 'right':
            return (current_heading - 90) % 360
        elif location == 'left':
            return (current_heading + 90) % 360
        else:
            return (current_heading + 180) % 360
    

    def edges(self):
        points = Polygon.Utils.pointList(self.polygon)

        edges = [];

        l = len(points)
        first_point = points[0]
        for index, point in enumerate(points):
            if index < (l - 1):
                next_point = points[index + 1]
                edges.append((point, next_point))
            else:
                edges.append((point, first_point))
        return edges
