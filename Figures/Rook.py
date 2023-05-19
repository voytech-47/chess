from Figures.Chessfigure import Chessfigure
from colors import red, green


class Rook(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 5, None)

    def __str__(self):
        return f"{green('R') if self.get_color() == 'white' else red('R')}"
        # return f"{'♖' if self.get_color() == 'white' else '♜'}"

    def isMovePossible(self, source, destination):
        if source.getX() == destination.getX() or source.getY() == destination.getY():
            return True
        return False