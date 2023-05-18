from Figures.Chessfigure import Chessfigure
from colors import red, green


class Queen(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 9, None)

    def __str__(self):
        return f"{green('Q') if self.get_color() == 'white' else red('Q')}"
        # return f"{'♕' if self.get_color() == 'white' else '♛'}"

    def isMovePossible(self, source, destination):
        if (source[0] == destination[0] or source[1] == destination[1]) or (
                source[0] - destination[0] == source[1] - destination[1]):
            return True
        return False
