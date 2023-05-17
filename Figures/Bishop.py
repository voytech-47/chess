from Chessfigure import Chessfigure


class Bishop(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 3)

    def __str__(self):
        return f'{self.get_color()} bishop'