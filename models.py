""" Modules containing cell and GridBoard class
Author: Daniel Kurniadi, 2020
"""

import numpy as np


class Cell(object):
	""" cell class representing each square in grid.
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self._distance = float('inf')
		self._heuristic = 0
		self.obstacle = False  # becomes obstacle cell

	@property
	def distance(self):
		return self._distance

	@distance.setter
	def distance(self, newdist):
		self._distance = newdist

	@property
	def heuristic(self):
		return self._heuristic

	@heuristic.setter
	def heuristic(self, newHeuristic):
		self._heuristic = newHeuristic

	def __hash__(self):
		return hash(self.x, self.y)

	def __eq__(self, other):
		if isinstance(other, (list, tuple)) and len(other) == 2:
			x, y = other
			return x == self.x and y == self.y
		elif isinstance(other, Cell):
			return (self.x, self.y) == (other.x, other.y)
		else:
			raise TypeError("Comparison operation not supported between "
							"instances of 'A' and '%s" % type(other))

	def __neq__(self, other):
		return not (self == other)


# Comment: scopenya kok ga jelas ya...
class GridBoard(object):
	""" GridBoard class representing a grid board which contains cell(s)
	"""
	neighbours4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	neighbours8 = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

	def __init__(self, numRows, numCols, neighbourMode='four'):
		""" Initialise GridBoard and populate with Cells of numRows x numCells
		:type numRows: int
		:type numCols: int
		:type neighbourMode: str; enum
		"""
		self._numRows = numRows
		self._numCols = numCols
		self._neighbourDirections = GridBoard.neighbours4

		# populate grids with cells
		x_axis = np.arange(0, numCols + 1).astype(int)
		y_axis = np.arange(0, numRows + 1).astype(int)
		meshgrid = np.meshgrid(x_axis, y_axis)
		self._cells = { Cell(x, y): 1 for xx, yy in zip(*meshgrid) for x, y in zip(xx, yy)}

		if neighbourMode == 'eight':
			self._neighbourDirections.extend(GridBoard.neighbours8)

	def get_size(self, format='WH'):
		""" Get size in format Width x Height or Heigh x Width
		:rtype (int, int)
		"""
		if format == 'WH':
			return (self._numRows, self._numCols)
		elif format == 'HW':
			return (self._numCols, self._numRows)
		else:
			ValueError("Gridboard size `format`: %s not recognized. Either use 'WH' or 'HW'.")

	def get(self, x, y):
		""" Get a cell given a coordinate if cell inside the grid boundary.
		If not in boundary then return None.

		:type x: int
		:type y: int
		:rtype Cell or None
		"""
		if (x, y) in self._cells:
			return self._cells[(x, y)]
		return None

	def getNeighbours(self, cell=None, x=-1, y=-1):
		""" Get neighbours of cell given the cell
		:type cell: Cell; optional
		:type x: int; optional
		:type y: int; optional
		:rtype List[Cell]
		"""
		if cell: 
			# cell object is passed instead of x, y
			x, y = cell.x, cell.y

		cell = cell or self._cells[(x, y)]

		# sanity check
		if not cell or cell not in self._cells or cell.obstacle:
			return []
		elif (isinstance(x, int) and isinstance(y, int)):
			return []

		neighbours = []
		for xDir, yDir in self._neighbourDirections:
			coor = (x + xDir, y + yDir)
			if coor in self._cells:
				cell = self._cells[coor]
				if not cell.obstacle:
					neighbours.append(cell)
		return neighbours
