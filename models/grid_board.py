import numpy as np
from .cell import Cell


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
		assert isinstance(numCols, int) and numCols > 0
		assert isinstance(numRows, int) and numRows > 0
		assert neighbourMode in ['four', 'eight']

		self._numRows = numRows
		self._numCols = numCols
		self._neighbourDirections = GridBoard.neighbours4.copy()
		self.cellMap = self.populateGrid(numRows, numCols)

		if neighbourMode == 'eight':
			self._neighbourDirections.extend(GridBoard.neighbours8)

	@staticmethod
	def populateGrid(numRows, numCols):
		# populate grids with cells
		x_axis = np.arange(0, numCols).astype(int)
		y_axis = np.arange(0, numRows).astype(int)
		meshgrid = np.meshgrid(x_axis, y_axis)
		return {(x, y): Cell(x, y) for xx, yy in zip(*meshgrid) for x, y in zip(xx, yy)}

	def getSize(self, format='WH'):
		""" Get size in format Width x Height or Heigh x Width
		:rtype (int, int)
		"""
		if format == 'WH':
			return (self._numCols, self._numRows)
		elif format == 'HW':
			return (self._numRows, self._numCols)
		else:
			ValueError("Gridboard size `format`: %s not recognized. Either use 'WH' or 'HW'.")

	def getCell(self, x, y):
		""" Get a cell given a coordinate if cell inside the grid boundary.
		If not in boundary then return None.

		:type x: int
		:type y: int
		:rtype Cell or None
		"""
		if (x, y) in self.cellMap:
			return self.cellMap[(x, y)]
		return None

	def getNeighbours(self, x=-1, y=-1, cell=None):
		""" Get neighbours of cell given the cell
		:type cell: Cell; optional
		:type x: int; optional
		:type y: int; optional
		:rtype List[Cell]
		"""
		if cell: 
			# cell object is passed instead of x, y
			x, y = cell.x, cell.y

		# sanity check
		if (x, y) not in self.cellMap or (cell and cell.obstacle == True):
			return []
		elif (isinstance(x, int) and isinstance(y, int)):
			return []

		neighbours = []
		for xDir, yDir in self._neighbourDirections:
			coor = (x + xDir, y + yDir)
			if coor in self.cellMap:
				neighcell = self.cellMap[coor]
				if not neighcell.obstacle and not neighcell.closed:
					neighbours.append(neighcell)
		return neighbours
