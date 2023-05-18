from Figures.Chessfigure import Chessfigure
from colors import red, green


class Knight(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 3, [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)])

    def __str__(self):
        return f"{green('N') if self.get_color() == 'white' else red('N')}"
        # return f"{'♘' if self.get_color() == 'white' else '♞'}"
