from Figures.Chessfigure import Chessfigure
from colors import red, green


class Knight(Chessfigure):
    _directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    def __init__(self, color):
        super().__init__(color, 3)

    def get_directions(self):
        return self._directions

    def set_directions(self, value):
        if value is not None:
            if self.get_color() == 'black':
                self._directions = [(-x, -y) for x, y in value]
            else:
                self._directions = value

    def __str__(self):
        return f"{green('N') if self.get_color() == 'white' else red('N')}"
        # return f"{'♘' if self.get_color() == 'white' else '♞'}"

    def is_move_possible(self, source, destination):
        directions = self.get_directions()
        for direction in directions:
            result = list(map(sum, zip([source.get_x(), source.get_y()], direction)))
            if result == [destination.get_x(), destination.get_y()]:
                return True
        return False
