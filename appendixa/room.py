from .segment import Segment
import Polygon, Polygon.Utils
from .vector import Vector
import random

class Room(Segment):
    def __init__(self, x, y, rotation=0) -> None:
        super().__init__(x, y)
        self.polygon = Polygon.Polygon(((x, y), (x, y+30), (x+30, y+30), (x+30, y)))
        self.polygon.rotate(rotation)

    def has_exits(self):
        return True
    
    def select_wall_segment(self, location, current_heading):
        print(f'Selecting wall segment for exit location {location}')
        print(f'Current heading is {current_heading}')

        heading_angle = self.direction_from_heading(location, current_heading)
        print(f'Heading angle is {heading_angle}')
        heading_vector = Vector.from_angle(heading_angle).getNormalised()
        print(f'Heading vector is {heading_vector}')
        midpoints = []
        
        center = self.polygon.center()
        print(f'Center is {center}')
        
        edges = Polygon.Utils.pointList(self.polygon)
        print(f'Edges are {edges}')
        closest_edge = edges[0]
        closest_distance = None

        for edge in self.edges():
            print(f'\tEdge is {edge}')
            edge_start = edge[0]
            edge_end = edge[1]
            
            midpoint_x = (edge_start[0] + edge_end[0]) / 2
            midpoint_y = (edge_start[1] + edge_end[1]) / 2

            print(f'\tMidpoint is {midpoint_x}, {midpoint_y}')

            midpoint_vector_x = midpoint_x - center[0]
            midpoint_vector_y = midpoint_y - center[1]
           
            midpoint_vector = Vector(midpoint_vector_x, midpoint_vector_y)
           
            print(f'\tMidpoint vector is {midpoint_vector}')
            midpoint_vector = midpoint_vector.getNormalised()
            print(f'\tNormalized Midpoint vector is {midpoint_vector}')
            
            distance = Vector.Distance(heading_vector, midpoint_vector)
            print(f'\tDistance is {distance}')
            if closest_distance is None or (distance < closest_distance):
                closest_distance = distance
                closest_edge = edge

        print(f'Closest edge is {closest_edge}, closest delta length is {closest_distance}')
        return closest_edge
