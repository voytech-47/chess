from Chessfigure import Chessfigure


class Queen(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 9)

    def __str__(self):
        return f'{self.get_color()} queen'