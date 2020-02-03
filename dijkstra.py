"""
"""
from heapq import heapify, heappop, heappush
# from models import GridBoard, Tile

class Dijkstra(object):
    """ Path finder algorithm handler
    """

    def __init__(self, grid, startCoor, endCoor, adjancentDist=1):
        xStart, yStart = startCoor
        xEnd, yEnd = endCoor

        self.adjancentDist = adjancentDist
        self.grid = grid
        self.startTile = self.grid.get(xStart, yStart)
        self.endTile = self.grid.get(xEnd, yEnd)
        self.reachedEnd = False

        self.heapQueue = heapify([(0, self.startTile)])
        self.trackRecords = {}

    def step(self):
        if not self.heapQueue: return None

        dist, currentTile = heappop(self.heapQueue)  # comment: heapq doesn't support key min, but this is redudant
        currentTile.closed = True

        if currentTile == self.endTile:
            self.reachedEnd = True
            return currentTile

        for neighbour in self.grid.getNeighbours(currentTile):
            if neighbour.closed == True: continue

            alt = dist + self.adjancentDist
            if alt < neighbour.distance:
                neighbour.distance = alt
                neighbour.opened = True
        return None
