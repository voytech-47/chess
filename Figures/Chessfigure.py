class Chessfigure:
    _directions = []
    _color = None
    _value = None

    def __init__(self, color, value, directions):
        self.set_color(color)
        self.set_value(value)
        self.set_directions(directions)

    def get_directions(self):
        return self._directions

    def set_directions(self, value):
        self._directions = value

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def isMoveLegal(self, destination):
        pass

    def moveFigure(self, destination):
        self.isMoveLegal(destination)
