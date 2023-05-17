class Cell:
    _x = None
    _y = None
    _figure = None

    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def placeFigure(self, figure):
        self._figure = figure

    def removeFigure(self):
        self._figure = None

