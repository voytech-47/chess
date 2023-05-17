from Chessfigure import Chessfigure


class King(Chessfigure):
    def __init__(self, piece_id, color):
        super().__init__(piece_id, color, 4)
