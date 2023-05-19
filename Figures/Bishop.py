from Figures.Chessfigure import Chessfigure
from colors import red, green


class Bishop(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 3, None)

    def __str__(self):
        return f"{green('B') if self.get_color() == 'white' else red('B')}"
        # return f"{'♗' if self.get_color() == 'white' else '♝'}"

    def isMovePossible(self, source, destination):
        if abs(source.getX() - destination.getX()) == abs(source.getY() - destination.getY()):
            return True
        return False
