import os

from Figures.Chessfigure import Chessfigure
from colors import red, green


class Queen(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 9)

    def __str__(self):
        if os.getenv("PYCHARM_HOSTED") is not None:
            return f"{green('Q') if self.get_color() == 'white' else red('Q')}"
        return f"{'♕' if self.get_color() == 'white' else '♛'}"

    def is_move_possible(self, source, destination):
        if (source.get_x() == destination.get_x() or source.get_y() == destination.get_y()) or (
                abs(source.get_x() - destination.get_x()) == abs(source.get_y() - destination.get_y())):
            return True
        return False
