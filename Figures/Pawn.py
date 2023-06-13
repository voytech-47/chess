from Figures.Chessfigure import Chessfigure
from colors import red, green


class Pawn(Chessfigure):
    _capturing_directions = None
    _directions = None

    def __init__(self, color):
        super().__init__(color, 1)
        if color == "white":
            self.set_capturing_directions([(1, 1), (-1, 1)])
            self.set_directions([(0, 1), (0, 2)])
        else:
            self.set_capturing_directions([(1, -1), (-1, -1)])
            self.set_directions([(0, -1), (0, -2)])

    def get_capturing_directions(self):
        return self._capturing_directions

    def set_capturing_directions(self, value):
        self._capturing_directions = value

    def get_directions(self):
        return self._directions

    def set_directions(self, directions):
        self._directions = directions

    def __str__(self):
        return f"{green('P') if self.get_color() == 'white' else red('P')}"
        # return f"{'♙' if self.get_color() == 'white' else '♟︎'}"

    def is_move_possible(self, source, destination):
        if source.get_x() == destination.get_x():
            directions = self.get_directions()
            for direction in directions:
                result = list(map(sum, zip([source.get_x(), source.get_y()], direction)))
                if result == [destination.get_x(), destination.get_y()]:
                    return True
            return False
        else:
            if destination.get_figure() is not None and destination.get_figure().get_color() != self.get_color():
                capturingDirections = self.get_capturing_directions()
                for direction in capturingDirections:
                    result = list(map(sum, zip([source.get_x(), source.get_y()], direction)))
                    if result == [destination.get_x(), destination.get_y()]:
                        return True
                return False
            return False

    def moved(self):
        if not self._hasMoved:
            try:
                self.get_directions().remove((0, 2))
            except ValueError:
                self.get_directions().remove((0, -2))
            self._hasMoved = True
