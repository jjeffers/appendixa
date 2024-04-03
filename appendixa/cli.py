"""CLI interface for appendixa project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

import random
import Polygon.IO
from .base import Room, AddRoom

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

Polygon.IO.writeSVG("map.svg", [segment.polygon for segment in segments])   

    
