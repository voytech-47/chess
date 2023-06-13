from Components.Cell import Cell
from Figures.Bishop import Bishop
from Figures.King import King
from Figures.Knight import Knight
from Figures.Pawn import Pawn
from Figures.Queen import Queen
from Figures.Rook import Rook
from colored import bg, attr

moved_background = bg(21)
reset_background = attr('reset')


class Board:
    board = [[] for i in range(8)]
    # turn = 0 -> white, turn = 1 -> black
    turn = 0
    _recently_moved = []
    points = {
        "white": 0,
        "black": 0
    }
    _captured_figures = []
    _kings = {
        "white": None,
        "black": None
    }

    def __init__(self):
        for x in range(8):
            for y in range(8):
                cell = Cell(x, y)
                self.board[y].append(cell)

    def get_king(self, color: str) -> Cell:
        return self._kings[color]

    def set_king(self, color: str, king: Cell):
        self._kings[color] = king

    def increase_points(self, player: str, amount: int):
        self.points[player] += amount

    def place_figures(self):
        for y in range(8):
            white_pawn = Pawn('white')
            self.board[1][y].place_figure(white_pawn)
            black_pawn = Pawn('black')
            self.board[-2][y].place_figure(black_pawn)

        for y in range(0, 8, 7):
            white_rook = Rook('white')
            self.board[0][y].place_figure(white_rook)
            black_rook = Rook('black')
            self.board[-1][y].place_figure(black_rook)

        for y in range(1, 7, 5):
            white_knight = Knight('white')
            self.board[0][y].place_figure(white_knight)
            black_knight = Knight('black')
            self.board[-1][y].place_figure(black_knight)

        for y in range(2, 6, 3):
            white_bishop = Bishop('white')
            self.board[0][y].place_figure(white_bishop)
            black_bishop = Bishop('black')
            self.board[-1][y].place_figure(black_bishop)

        white_queen = Queen('white')
        self.board[0][3].place_figure(white_queen)
        black_queen = Queen('black')
        self.board[-1][3].place_figure(black_queen)
        white_king = King('white')
        self.board[0][4].place_figure(white_king)
        self.set_king("white", self.board[0][4])
        black_king = King('black')
        self.board[-1][4].place_figure(black_king)
        self.set_king("black", self.board[-1][4])

    def get_board(self) -> list:
        return self.board

    def change_turn(self):
        self.turn = (self.turn + 1) % 2

    def get_turn(self) -> str:
        if self.turn:
            return "black"
        return "white"

    @staticmethod
    def translate_xy(xy: str) -> list:
        x = ord(xy[0]) - 97
        y = int(xy[1]) - 1
        if x not in range(0, 8) or y not in range(0, 8):
            raise Exception("Index out of the board")
        return [x, y]

    def __str__(self):
        for row in list(reversed(self.get_board())):
            for cell in row:
                if cell.has_moved():
                    print(moved_background, end='')
                if cell.get_figure() is None:
                    if cell.has_moved():
                        print(' ' + reset_background, end=' ')
                    else:
                        print(' ', end=' ')
                else:
                    print(cell, end=' ')
                print(reset_background, end='')
            print()
        print('\n|--------------|')
        return ''

    def is_move_legal(self, source_cell: Cell, destination_cell: Cell) -> bool:
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
            if self.check_vertical(source_cell, destination_cell):
                return True
            return False
        elif source_cell.get_y() == destination_cell.get_y():
            if self.check_horziontal(source_cell, destination_cell):
                return True
            return False
        else:
            if self.check_diagonal(source_cell, destination_cell):
                return True
            return False

    def check_turn(self, source_cell: Cell):
        if source_cell.get_figure().get_color() != self.get_turn():
            raise Exception("Not your turn")

    def check_for_check(self, turn: str) -> bool:
        king = self.get_king(turn)
        if self.check_vartical_check(king) or self.check_horizontal_check(king) or self.check_diagonal_check(king):
            return True
        return False

    def check_horizontal_check(self, king: Cell):
        row = self.get_board()[king.get_y()]
        for cell in row:
            if cell.get_figure() is not None and cell.get_figure().is_move_possible(cell, king) and cell is not king:
                return True
        return False

    def check_vartical_check(self, king: Cell):
        board = self.get_board()
        x = king.get_x()
        for i in range(8):
            cell = board[i][x]
            if cell.get_figure() is not None and cell.get_figure().is_move_possible(cell, king) and cell is not king:
                return True
        return False

    def check_diagonal_check(self, king: Cell):
        board = self.get_board()
        x = king.get_x()
        y = king.get_y()
        while x > 0 and y > 0:
            cell = board[y - 1][x - 1]
            if cell.get_figure() is not None and cell.get_figure().is_move_possible(cell, king):
                return True
            x, y = x - 1, y - 1

        x = king.get_x()
        y = king.get_y()
        while x < 7 and y < 7:
            cell = board[y + 1][x + 1]
            if cell.get_figure() is not None and cell.get_figure().is_move_possible(cell, king):
                return True
            x, y = x + 1, y + 1

        x = king.get_x()
        y = king.get_y()
        while x > 0 and y < 7:
            cell = board[y + 1][x - 1]
            if cell.get_figure() is not None and cell.get_figure().is_move_possible(cell, king):
                return True
            x, y = x - 1, y + 1

        x = king.get_x()
        y = king.get_y()
        while x < 7 and y > 0:
            cell = board[y - 1][x + 1]
            if cell.get_figure() is not None and cell.get_figure().is_move_possible(cell, king):
                return True
            x, y = x + 1, y + 1

        return False

    def check_vertical(self, source: Cell, destination: Cell) -> bool:
        board = self.get_board()
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

    def check_horziontal(self, source: Cell, destination: Cell) -> bool:
        board = self.get_board()
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

    def check_diagonal(self, source: Cell, destination: Cell) -> bool:
        board = self.get_board()
        stop = abs(source.get_x() - destination.get_x())
        if source.get_x() < destination.get_x() and source.get_y() < destination.get_y():
            for xy in range(stop):
                if board[source.get_y() + xy + 1][source.get_x() + xy + 1].get_figure() is not None:
                    if board[source.get_y() + xy + 1][source.get_x() + xy + 1] \
                            .get_figure().get_color() == source.get_figure().get_color():
                        return False
            return True
        elif source.get_x() < destination.get_x() and source.get_y() > destination.get_y():
            for xy in range(stop):
                if board[source.get_y() - xy - 1][source.get_x() + xy + 1].get_figure() is not None:
                    return False
            return True
        elif source.get_x() > destination.get_x() and source.get_y() > destination.get_y():
            for xy in range(stop):
                if board[source.get_y() - 1 - xy][source.get_x() - 1 - xy].get_figure() is not None:
                    return False
            return True
        elif source.get_x() > destination.get_x() and source.get_y() < destination.get_y():
            for xy in range(stop):
                if board[source.get_y() + 1 + xy][source.get_x() - 1 - xy].get_figure() is not None:
                    return False
            return True

    def reset_recently_moved(self):
        for cell in self._recently_moved:
            cell.set_has_moved(False)
        self._recently_moved.clear()

    def add_recently_moved(self, source: Cell, destination: Cell):
        self._recently_moved.append(source)
        self._recently_moved.append(destination)

    def move(self, source: str, destination: str):
        self.reset_recently_moved()
        source = self.translate_xy(source)
        destination = self.translate_xy(destination)
        source_cell = self.get_board()[source[1]][source[0]]
        destination_cell = self.get_board()[destination[1]][destination[0]]
        self.check_turn(source_cell)
        if not source_cell.get_figure().is_move_possible(source_cell, destination_cell) or source == destination:
            raise Exception("Move not possible")
        if not self.is_move_legal(source_cell, destination_cell):
            raise Exception("Move not legal")
        # if not self.checkForCheck(self.getTurn()):
        #     raise Exception("There is a check")
        if destination_cell.get_figure() is not None:
            self.capture(source_cell, destination_cell)
        destination_cell.place_figure(source_cell.get_figure())
        destination_cell.set_has_moved(True)
        source_cell.remove_figure()
        source_cell.set_has_moved(True)
        self.add_recently_moved(source_cell, destination_cell)
        self.change_turn()
        print(self)

    def capture(self, source: Cell, destination: Cell):
        self.increase_points(source.get_figure().get_color(), destination.get_figure().get_value())
        print(f"{source.get_figure().get_color()} player: +{destination.get_figure().get_value()} point(s)")
