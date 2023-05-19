class Cell:
    _x = None
    _y = None
    _figure = None
    _hasMoved = False

    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def hasMoved(self):
        return self._hasMoved

    def set_hasMoved(self, value):
        self._hasMoved = value

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getXY(self):
        return [self.getX(), self.getY()]

    def placeFigure(self, figure):
        self._figure = figure

    def removeFigure(self):
        self._figure.moved()
        self._figure = None

    def getFigure(self):
        return self._figure

    def __str__(self):
        if self.getFigure() is None:
            return ' '
        return str(self.getFigure())
