import numpy as np
from models import Cell, GridBoard


def test_populate_board():
    numRows = 100  # x-axis
    numCols = 80   # y-axis
    cellMaps = GridBoard.populateGrid(numRows, numCols)

    # check number of cells in grid
    assert len(cellMaps) == (numCols * numRows)

    # check if the coordinate of each cell is correct
    for y in range(numRows):
        for x in range(numCols):
            assert (cellMaps.get(y,x) is not None)


def test_get_size():
    numRows = 100  # x-axis
    numCols = 80   # y-axis
    grid = GridBoard(numRows, numCols)

    width, height = grid.getSize(format='WH')

    assert width == numCols
    assert height == numRows


def test_get_neighbours_four_by_coor():
    numRows = 100
    numCols = 80
    x, y = 40, 50
    grid = GridBoard(numRows, numCols, neighbourMode='four')
    neighboursCoor = [(40,51), (41,50), (39,50), (40,49)]

    # get neighbours by passing coordinate
    neighbours = grid.getNeighbours(x=x, y=y)
    for neighcell in neighbours:
        x2, y2 = neighcell.x, neighcell.y
        assert (x2,y2) in neighboursCoor


def test_get_neighbours_four_by_cell():
    numRows = 100
    numCols = 80
    x, y = 40, 50
    neighboursCoor = [(40,51), (41,50), (39,50), (40,49)]
    grid = GridBoard(numRows, numCols, neighbourMode='four')

    # get neighbours by passing cell
    cell = Cell(x, y)
    neighbours = grid.getNeighbours(cell=cell)
    for neighcell in neighbours:
        x2, y2 = neighcell.x, neighcell.y
        assert (x2,y2) in neighboursCoor


def test_get_neighbours_eight_by_coor():
    numRows = 100
    numCols = 80
    x, y = 40, 50
    neighboursCoor = [(40,51), (41,50), (39,50), (40,49),
                      (39,49), (41,51), (39,51), (41,49)]
    grid = GridBoard(numRows, numCols, neighbourMode='eight')

    # get neighbours by passing coordinate
    neighbours = grid.getNeighbours(x=x, y=y)
    for neighcell in neighbours:
        x2, y2 = neighcell.x, neighcell.y
        assert (x2, y2) in neighboursCoor


def test_get_neighbours_eight_by_coor():
    numRows = 100
    numCols = 80
    x, y = 40, 50
    neighboursCoor = [(40,51), (41,50), (39,50), (40,49),
                      (39,49), (41,51), (39,51), (41,49)]
    grid = GridBoard(numRows, numCols, neighbourMode='eight')

    # get neighbours by passing cell
    cell = Cell(x, y)
    neighbours = grid.getNeighbours(cell=cell)
    for neighcell in neighbours:
        x2, y2 = neighcell.x, neighcell.y
        assert (x2, y2) in neighboursCoor
