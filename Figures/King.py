from Figures.Chessfigure import Chessfigure
from colors import red, green


class King(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 4, None)

    def __str__(self):
        return f"{green('K') if self.get_color() == 'white' else red('K')}"
        # return f"{'♔' if self.get_color() == 'white' else '♚'}"

    def isMovePossible(self, source, destination):
        if abs(source[0] - destination[0]) <= 1 and abs(source[1] - destination[1]) <= 1:
            return True
        return False
