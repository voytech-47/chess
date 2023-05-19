from Figures.Chessfigure import Chessfigure
from colors import red, green


class Queen(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 9, None)

    def __str__(self):
        return f"{green('Q') if self.get_color() == 'white' else red('Q')}"
        # return f"{'♕' if self.get_color() == 'white' else '♛'}"

    def isMovePossible(self, source, destination):
        if (source.getX() == destination.getX() or source.getY() == destination.getY()) or (
                abs(source.getX() - destination.getX()) == abs(source.getY() - destination.getY())):
            return True
        return False
