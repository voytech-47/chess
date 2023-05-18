from Figures.Chessfigure import Chessfigure


class Rook(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 5, [(0, 0)])

    def __str__(self):
        return f"{'♖' if self.get_color() == 'white' else '♜'}"
