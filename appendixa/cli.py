"""CLI interface for appendixa project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

import random
import Polygon.Utils, Polygon.IO
from appendixa import *
from .base import *
import pygame

def Capture(display,name,pos,size): # (pygame Surface, String, tuple, tuple)
    image = pygame.Surface(size)  # Create image surface
    image.blit(display,(0,0),(pos,size))  # Blit portion of the display to the image
    pygame.image.save(image,name)  # Save the image to the disk

def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m appendixa` and `$ appendixa `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """

from collections import deque
generation_queue = deque()

generation_queue.append(AddRoom(0, 0))
segments = []
current_heading = 0

while len(generation_queue) > 0:
    current_action = generation_queue.popleft()
    
    current_action.execute(generation_queue, segments, current_heading)

pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((0, 0, 0))
 
for poly in [segment.polygon for segment in segments]:
    points = Polygon.Utils.pointList(poly)
    points = [(int(x+300), int(y+300)) for x, y in points]
    pygame.draw.polygon(window, (255, 255, 255), points)

# Draws the surface object to the screen.
#pygame.display.flip()

# Capture a screenshot and save it as a PNG file
pygame.image.save(window, "screenshot.png")
# Quit Pygame
pygame.quit()




    
