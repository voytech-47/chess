from Components import Cell, Board


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

    def is_move_legal(self, source_cell: Cell, destination_cell: Cell, board: Board) -> bool:
        try:
            if source_cell.get_figure().get_color() == destination_cell.get_figure().get_color():
                return False
        except AttributeError:
            pass

        if source_cell.get_figure().is_knight() or source_cell.get_figure().is_pawn():
            if source_cell.get_figure().is_move_possible(source_cell, destination_cell):
                return True
            return False

        if source_cell.get_x() == destination_cell.get_x():
            if self.check_vertical(source_cell, destination_cell, board):
                return True
            return False
        elif source_cell.get_y() == destination_cell.get_y():
            if self.check_horziontal(source_cell, destination_cell, board):
                return True
            return False
        else:
            if self.check_diagonal(source_cell, destination_cell, board):
                return True
            return False

    def check_vertical(self, source: Cell, destination: Cell, board: Board) -> bool:
        stop = abs(source.get_y() - destination.get_y())
        if source.get_y() < destination.get_y():
            for y in range(stop):
                if board[source.get_y() + 1 + y][source.get_x()].get_figure() is not None:
                    return False
            return True
        else:
            for y in range(stop):
                if board[source.get_y() - 1 - y][source.get_x()].get_figure() is not None:
                    return False
            return True

    def check_horziontal(self, source: Cell, destination: Cell, board: Board) -> bool:
        stop = abs(source.get_x() - destination.get_x())
        if source.get_x() < destination.get_x():
            for x in range(stop):
                if board[source.get_y()][source.get_x() + 1 + x].get_figure() is not None:
                    return False
            return True
        else:
            for x in range(stop):
                if board[source.get_y()][source.get_x() - 1 - x].get_figure() is not None:
                    return False
            return True

    def check_diagonal(self, source: Cell, destination: Cell, board: Board) -> bool:
        stop = abs(source.get_x() - destination.get_x())
        if source.get_x() < destination.get_x() and source.get_y() < destination.get_y():
            for xy in range(stop):
                current_cell = board[source.get_y() + xy + 1][source.get_x() + xy + 1]
                if current_cell.get_figure() is not None:
                    if current_cell == destination:
                        return True
                    return False
            return True
        elif source.get_x() < destination.get_x() and source.get_y() > destination.get_y():
            for xy in range(stop):
                current_cell = board[source.get_y() - xy - 1][source.get_x() + xy + 1]
                if current_cell.get_figure() is not None:
                    if current_cell == destination:
                        return True
                    return False
            return True
        elif source.get_x() > destination.get_x() and source.get_y() > destination.get_y():
            for xy in range(stop):
                current_cell = board[source.get_y() - 1 - xy][source.get_x() - 1 - xy]
                if current_cell.get_figure() is not None:
                    if current_cell == destination:
                        return True
                    return False
            return True
        elif source.get_x() > destination.get_x() and source.get_y() < destination.get_y():
            for xy in range(stop):
                current_cell = board[source.get_y() + 1 + xy][source.get_x() - 1 - xy]
                if current_cell.get_figure() is not None:
                    if current_cell == destination:
                        return True
                    return False
            return True
