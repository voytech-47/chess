import os

from Figures.Chessfigure import Chessfigure
from colors import red, green


class King(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 4)

    def __str__(self):
        if os.getenv("PYCHARM_HOSTED") is not None:
            return f"{green('K') if self.get_color() == 'white' else red('K')}"
        return f"{'♔' if self.get_color() == 'white' else '♚'}"

    def is_move_possible(self, source, destination):
        if abs(source.get_x() - destination.get_x()) <= 1 and abs(source.get_y() - destination.get_y()) <= 1:
            return True
        return False
