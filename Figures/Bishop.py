from Figures.Chessfigure import Chessfigure
from colors import red, green
import os


class Bishop(Chessfigure):
    def __init__(self, color):
        super().__init__(color, 3)

    def __str__(self):
        if os.getenv("PYCHARM_HOSTED") is not None:
            return f"{green('B') if self.get_color() == 'white' else red('B')}"
        return f"{'♗' if self.get_color() == 'white' else '♝'}"



    def is_move_possible(self, source, destination):
        if abs(source.get_x() - destination.get_x()) == abs(source.get_y() - destination.get_y()):
            return True
        return False
