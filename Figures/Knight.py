from Figures.Chessfigure import Chessfigure

class Knight(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 3, [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)])

    def __str__(self):
        return f"{'♘' if self.get_color() == 'white' else '♞'}"