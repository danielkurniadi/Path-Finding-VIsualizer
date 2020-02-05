import pygame
import time

BORDER_COLOR = (115, 194, 251)

EMPTY_CELL_COLOR = (255, 255, 255)
BLOCKED_CELL_COLOR = (29, 41, 81)

CLOSED_SET_COLOR_1 = (17, 30, 108)


class GridView(object):
    """ Grid View handler class
    """

    def __init__(self, size, cellSize, background_color=(255,255,255)):
        """
        :type size: (int, int) representing (width, height)
        :type cellSize: (int, int) representing (cellWidth, cellHeight)
        :type background_color: (int, int, int) representing (r,g,b)
        """
        self.width, self.height = size
        self.cellWidth, self.cellHeight = cellSize

        self.numRows = self.width // self.cellWidth
        self.numCols = self.height // self.cellHeight

        self._pygame_screen = pygame.display.set_mode((self.width, self.height))
        self._pygame_screen.fill(background_color)

        self.reset()

    def reset(self):
        """ Reset view to initial view
        """
        for i in range(self.numCols+1):
            for j in range(self.numRows+1):
                self._draw_cell(i, j, EMPTY_CELL_COLOR)

    # ------------------------
    # Draw Cell Methods
    # ------------------------

    def draw_closed_cells(self, closedSet):
        """
        :type closedSet: Cell
        """
        for cell in closedSet:
            self._draw_cell(cell.x, cell.y, CLOSED_SET_COLOR_1)

    def draw_solution_cells(self, solutionCells):
        pass

    def _draw_cell(self, i, j, color):
        """
        :type i: int
        :type j: int
        :type color: (int, int, int) representing (r, g, b)
        """
        # fill rectangle with color
        pygame.draw.rect(self._pygame_screen, color, 
                        (i * self.cellWidth, j * self.cellHeight, self.cellWidth, self.cellHeight), 0)
        # border line with black
        pygame.draw.rect(self._pygame_screen, BORDER_COLOR,
                        (i * self.cellWidth, j * self.cellHeight, self.cellWidth, self.cellHeight), 1)
        pygame.display.update()


if __name__ == "__main__":
    grid = GridView((400, 400), (16, 16))
    grid.reset()

    pygame.init()
    pygame.display.update()

    closedSet = [Cell(x,1) for x in range(400)]

    while True:
        grid.draw_closed_cells(closedSet)
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:
            pygame.quit()
