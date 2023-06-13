from Figures.Chessfigure import Chessfigure
from colors import red, green


class Rook(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 5)

    def __str__(self):
        return f"{green('R') if self.get_color() == 'white' else red('R')}"
        # return f"{'♖' if self.get_color() == 'white' else '♜'}"

    def is_move_possible(self, source, destination):
        if source.get_x() == destination.get_x() or source.get_y() == destination.get_y():
            return True
        return False
