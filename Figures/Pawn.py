from Figures.Chessfigure import Chessfigure
from colors import red, green


class Pawn(Chessfigure):
    _capturingDirections = None

    def __init__(self, color):
        super().__init__(color, 1, [(0, 1), (0, 2)])
        if color == "white":
            self.set_capturingDirections([(1, 1), (-1, 1)])
        else:
            self.set_capturingDirections([(1, -1), (-1, -1)])

    def get_capturingDirections(self):
        return self._capturingDirections

    def set_capturingDirections(self, value):
        self._capturingDirections = value

    def set_directions(self, value):
        if self.get_color() == 'black':
            self._directions = [(-x, -y) for x, y in value]
        else:
            self._directions = value

    def __str__(self):
        return f"{green('P') if self.get_color() == 'white' else red('P')}"
        # return f"{'♙' if self.get_color() == 'white' else '♟︎'}"

    def isMovePossible(self, source, destination):
        if source.getX() == destination.getX():
            directions = self.get_directions()
            for direction in directions:
                result = list(map(sum, zip([source.getX(), source.getY()], direction)))
                if result == [destination.getX(), destination.getY()]:
                    return True
            return False
        else:
            if destination.getFigure() is not None and destination.getFigure().get_color() != self.get_color():
                capturingDirections = self.get_capturingDirections()
                for direction in capturingDirections:
                    result = list(map(sum, zip([source.getX(), source.getY()], direction)))
                    if result == [destination.getX(), destination.getY()]:
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
