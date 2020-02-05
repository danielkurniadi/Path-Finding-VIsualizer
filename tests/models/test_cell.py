import math
from models import Cell


def test_create_cell():
    x, y = 100, 100
    cell = Cell(x, y)

    assert cell.x == x
    assert cell.y == y
    assert cell.distance == float('inf')
    assert cell.heuristic == 0


def test_change_cell_dist():
    cell = Cell(0, 0)
    distance = 1024
    cell.distance = distance
    assert cell.distance == distance


def test_change_cell_heuristic():
    cell = Cell(0, 0)
    heuristic = math.sqrt(24 + 7)
    cell.heuristic = heuristic
    assert cell.heuristic == heuristic


def test_cell_equality():
    assert Cell(100,100) == Cell(100,100)
    assert Cell(0,0) == Cell(0,0)
    assert Cell(-100,100) == Cell(-100,100)


def test_cell_inequality():
    assert Cell(-100,100) != Cell(0,100)
    assert Cell(100,-100) != Cell(100,100)
