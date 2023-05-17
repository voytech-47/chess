from Chessfigure import Chessfigure


class Rook(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 5)

    def __str__(self):
        return f'{self.get_color()} rook'
