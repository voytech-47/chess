from Figures.Chessfigure import Chessfigure
from colors import red, green


class Pawn(Chessfigure):

    def __init__(self, color):
        super().__init__(color, 1, [(0, 1), (0, 2)])

    def set_directions(self, value):
        if self.get_color() == 'black':
            self._directions = [(-x, -y) for x, y in value]
        else:
            self._directions = value

    def __str__(self):
        return f"{green('P') if self.get_color() == 'white' else red('P')}"
        # return f"{'♙' if self.get_color() == 'white' else '♟︎'}"

    def moved(self):
        self._hasMoved = True
        try:
            self.get_directions().remove((0, 2))
        except ValueError:
            self.get_directions().remove((0, -2))
