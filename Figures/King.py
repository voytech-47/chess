from Figures.Chessfigure import Chessfigure


class King(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 4, [(0, 0)])

    def __str__(self):
        return f'{self.get_color()} king'