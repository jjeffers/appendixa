from appendixa.vector import Vector

def test_vector_east():
    v = Vector(0)
    assert v.x == 1 and v.y == 0

def test_vector_north():
    v = Vector(90)
    assert v.x == 0 and v.y == 1

def test_vector_west():
    v = Vector(180)
    assert v.x == -1 and v.y == 0

def test_vector_south():
    v = Vector(270)
    assert v.x == 0 and v.y == -1