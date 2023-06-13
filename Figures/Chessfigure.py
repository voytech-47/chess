class Chessfigure:
    _directions = []
    _color = None
    _value = None
    _hasMoved = False

    def __init__(self, color, value):
        self.set_color(color)
        self.set_value(value)

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

    def is_knight(self):
        if self.__class__.__name__ == "Knight":
            return True
        return False

    def is_pawn(self):
        if self.get_value() == 1:
            return True
        return False
