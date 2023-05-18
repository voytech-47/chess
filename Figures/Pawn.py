from Figures.Chessfigure import Chessfigure


class Pawn(Chessfigure):

    def __init__(self, color):
        super().__init__(color, 1, [(0, 1), (0, 2)])

    def __str__(self):
        return f"{'♙' if self.get_color() == 'white' else '♟︎'}"

    def moved(self):
        self._hasMoved = True
        self.get_directions().remove((0, 2))
