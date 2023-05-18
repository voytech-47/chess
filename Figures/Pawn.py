from Figures.Chessfigure import Chessfigure


class Pawn(Chessfigure):
    _hasMoved = False

    def __init__(self, color):
        super().__init__(color, 1, [(0, 1), (0, 2)])

    def __str__(self):
        return f'{self.get_color()} pawn'
