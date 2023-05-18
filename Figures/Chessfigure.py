class Chessfigure:
    _directions = []
    _color = None
    _value = None
    _hasMoved = False

    def __init__(self, color, value, directions):
        self.set_color(color)
        self.set_value(value)
        self.set_directions(directions)

    def get_directions(self):
        return self._directions

    def set_directions(self, value):
        if self.get_color() == 'black':
            self._directions = [(-x, -y) for x, y in value]
        else:
            self._directions = value

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def moved(self):
        self._hasMoved = True

    def isMovePossible(self, source, destination):
        directions = self.get_directions()
        for direction in directions:
            result = list(map(sum, zip(source, direction)))
            if result == destination:
                return True
        return False
