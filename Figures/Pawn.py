from Chessfigure import Chessfigure


class Pawn(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 1)

    def __str__(self):
        return f'{self.get_color()} pawn'
