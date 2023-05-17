class Chessfigure:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def get_color(self):
        return self.color

    def set_color(self, value):
        self.color = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
