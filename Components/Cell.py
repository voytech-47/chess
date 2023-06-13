class Cell:
    _x = None
    _y = None
    _figure = None
    _has_moved = False

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def has_moved(self):
        return self._has_moved

    def set_has_moved(self, value):
        self._has_moved = value

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_xy(self):
        return [self.get_x(), self.get_y()]

    def place_figure(self, figure):
        self._figure = figure

    def remove_figure(self):
        self._figure.moved()
        self._figure = None

    def get_figure(self):
        return self._figure

    def __str__(self):
        if self.get_figure() is None:
            return ' '
        return str(self.get_figure())
