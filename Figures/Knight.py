from Chessfigure import Chessfigure

class Knight(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 3)

    def __str__(self):
        return f'{self.get_color()} knight'