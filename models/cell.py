""" Modules containing Cell class
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
		self.opened = False
		self.closed = 0        # zero means not in closedSet yet

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
		return hash((self.x, self.y))

	def __eq__(self, other):
		if isinstance(other, Cell):
			return (self.x, self.y) == (other.x, other.y)
		else:
			raise TypeError("Comparison operation not supported between "
							"instances of 'Cell' and '%s" % type(other))

	def __neq__(self, other):
		return not (self == other)

	def __str__(self):
		return "<Cell: %d, %d>" % (self.x, self.y)
