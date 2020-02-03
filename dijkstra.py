"""
"""

from heapq import heapify, heappop, heappush


class Dijkstra(object):
    """ Path finder algorithm handler
    """

    def __init__(self, grid, startCoor, endCoor, adjancentDist=1):
        """ Initialise Dijkstra solver for new problem
        :type grid: GridBoard
        :type startCoor: int
        :type encCoor: int
        :type adjacentDist: int
        """
        assert len(startCoor) == 2
        assert len(endCoor) == 2
        xStart, yStart = startCoor
        xEnd, yEnd = endCoor

        self.adjancentDist = adjancentDist
        self.grid = grid
        self.startTile = self.grid.get(xStart, yStart)
        self.endTile = self.grid.get(xEnd, yEnd)

        # checking if valid start and end
        if not self.startTile:
            raise ValueError("Start position is out of grid bound or invalid: " + str(startCoor))

        if not self.endTile:
            raise ValueError("End goal position is out of grid bound or invalid: " + str(endCoor))

        # setup state and track record
        self.openSet = heapify([(0, self.startTile)])
        self.closedSet = set()
        self.trackRecords = {}
        self.reachedEnd = False

    def step(self):
        """ Dijkstra per step implementation
        :rtype (List[Cell], Set{Cell}): data structures representing path finding state
        """
        if not self.openSet or self.reachedEnd == True:
            return self.openSet, self.closedSet

        dist, currentCell = heappop(self.openSet)  # comment: heapq doesn't support key min, but this is redudant
        self.closedSet.add(currentCell)

        if currentCell == self.endTile:
            self.reachedEnd = True
            return currentCell

        for neighbour in self.grid.getNeighbours(currentCell):
            if currentCell in self.closedSet: continue

            alt = dist + self.adjancentDist
            if alt < neighbour.distance:
                neighbour.distance = alt
                heappush(self.openSet, (alt, neighbour))

        return self.openSet, self.closedSet  # state of the path-finding
