from appendixa.vector import Vector

def test_vector_east():
    v = Vector.from_angle(0)
    assert v.x == 1 and v.y == 0

def test_vector_north():
    v = Vector.from_angle(90)
    assert v.x == 0 and v.y == 1

def test_vector_west():
    v = Vector.from_angle(180)
    assert v.x == -1 and v.y == 0

def test_vector_south():
    v = Vector.from_angle(270)
    assert v.x == 0 and v.y == -1