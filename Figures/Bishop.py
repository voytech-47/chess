from Figures.Chessfigure import Chessfigure
from colors import red, green


class Bishop(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 3, None)

    def __str__(self):
        return f"{green('B') if self.get_color() == 'white' else red('B')}"
        # return f"{'♗' if self.get_color() == 'white' else '♝'}"

    def isMovePossible(self, source, destination):
        if source[0] - destination[0] == source[1] - destination[1]:
            return True
        return False
