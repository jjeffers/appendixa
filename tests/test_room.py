from appendixa.room import Room
from appendixa.base import EAST, NORTH, WEST, SOUTH
import pytest

EAST_WALL = ((30, 30), (30, 0))
NORTH_WALL = ((0, 30), (30, 30))
WEST_WALL = ((0, 0), (0, 30))
SOUTH_WALL = ((30, 0), (0,0))

@pytest.fixture
def room():
    return Room(0, 0)

@pytest.mark.parametrize(
    "location,heading,expected",
    (
        ('opposite', EAST, EAST_WALL),
        ('opposite', NORTH, NORTH_WALL),
        ('opposite', WEST, WEST_WALL),
        ('opposite', SOUTH, SOUTH_WALL),
        ('left', EAST, NORTH_WALL),
        ('left', NORTH, WEST_WALL),
        ('left', WEST, SOUTH_WALL),
        ('left', SOUTH, EAST_WALL),
        ('right', EAST, SOUTH_WALL),
        ('right', NORTH, EAST_WALL),
        ('right', WEST, NORTH_WALL),
        ('right', SOUTH, WEST_WALL),
        ('same', EAST, WEST_WALL),
        ('same', NORTH, SOUTH_WALL),
        ('same', WEST, EAST_WALL),
        ('same', SOUTH, NORTH_WALL)
    ),
)
def test_room_wall_selection(room, location, heading, expected):
    assert room.select_wall_segment(location, heading) == expected
