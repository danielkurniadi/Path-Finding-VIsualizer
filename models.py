""" Modules containing Tile and GridBoard class
Author: Daniel Kurniadi, 2020
"""

import numpy as np


class Tile(object):
	""" Tile class representing each square in grid.
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self._distance = float('inf')
		self._heuristic = 0

		self.closed = False    # has been visited in closedSet
		self.opened = False    # has been considered in openSet
		self.obstacle = False  # becomes obstacle tile

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
		elif isinstance(other, Tile):
			return (self.x, self.y) == (other.x, other.y)
		else:
			raise TypeError("Comparison operation not supported between "
							"instances of 'A' and '%s" % type(other))

	def __neq__(self, other):
		return not (self == other)


# Comment: scopenya kok ga jelas ya...
class GridBoard(object):
	""" GridBoard class representing a grid board which contains Tile(s)
	"""
	neighbours4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	neighbours8 = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

	def __init__(self, tileRows, tileCols, neighbourMode='four'):
		"""
		"""
		self._tileRows = tileRows
		self._tileCols = tileCols
		self._neighbourDirections = GridBoard.neighbours4

		# populate grids with tiles
		x_axis = np.arange(0, tileCols + 1).astype(int)
		y_axis = np.arange(0, tileRows + 1).astype(int)
		meshgrid = np.meshgrid(x_axis, y_axis)
		self._tiles = { Tile(x, y): 1 for xx, yy in zip(*mesh) for x, y in zip(xx, yy)}

		if neighbourMode == 'eight':
			self._neighbourDirections.extend(GridBoard.neighbours8)

	def get_size(self, format='WH'):
		""" Get size in format Width x Height or Heigh x Width
		:rtype (int, int)
		"""
		if format == 'WH':
			return (self._tileRows, self._tileCols)
		elif format == 'HW':
			return (self._tileCols, self._tileRows)
		else:
			ValueError("Gridboard size `format`: %s not recognized. Either use 'WH' or 'HW'.")

	def get(self, x, y):
		if x, y in self._tiles:
			return self._tiles([x, y])
		return None

	def getNeighbours(self, tile):
		x, y = tile.x, tile.y
		neighbourTiles = []
		for xDir, yDir in self._neighbourDirections:
			if (x + xDir, y + yDir) in self._tiles:
				tile = self._tiles[(x + xDir, y + yDir)]
				neighbourTiles.append(tile)
		return neighbourTiles
