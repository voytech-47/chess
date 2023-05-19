from Components.Cell import Cell
from Figures.Bishop import Bishop
from Figures.King import King
from Figures.Knight import Knight
from Figures.Pawn import Pawn
from Figures.Queen import Queen
from Figures.Rook import Rook
from colored import bg, attr

moved = bg(101)
reset = attr('reset')


class Borad:
    board = [[] for i in range(8)]
    # turn = 0 -> white, turn = 1 -> black
    turn = 0
    _recentlyMoved = []
    points = {
        "white": 0,
        "black": 0
    }
    _capturedFigures = []
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

    def increacePoints(self, player: str, amount: int):
        self.points[player] += amount

    def placeFigures(self):
        for y in range(8):
            whitePawn = Pawn('white')
            self.board[1][y].placeFigure(whitePawn)
            blackPawn = Pawn('black')
            self.board[-2][y].placeFigure(blackPawn)

        for y in range(0, 8, 7):
            whiteRook = Rook('white')
            self.board[0][y].placeFigure(whiteRook)
            blackRook = Rook('black')
            self.board[-1][y].placeFigure(blackRook)

        for y in range(1, 7, 5):
            whiteKnight = Knight('white')
            self.board[0][y].placeFigure(whiteKnight)
            blackKnight = Knight('black')
            self.board[-1][y].placeFigure(blackKnight)

        for y in range(2, 6, 3):
            whiteBishop = Bishop('white')
            self.board[0][y].placeFigure(whiteBishop)
            blackBishop = Bishop('black')
            self.board[-1][y].placeFigure(blackBishop)

        whiteQueen = Queen('white')
        self.board[0][3].placeFigure(whiteQueen)
        blackQueen = Queen('black')
        self.board[-1][3].placeFigure(blackQueen)
        whiteKing = King('white')
        self.board[0][4].placeFigure(whiteKing)
        self.set_king("white", self.board[0][4])
        blackKing = King('black')
        self.board[-1][4].placeFigure(blackKing)
        self.set_king("black", self.board[-1][4])

    def get_board(self) -> list:
        return self.board

    def changeTurn(self):
        self.turn = (self.turn + 1) % 2

    def getTurn(self) -> str:
        if self.turn:
            return "black"
        return "white"

    @staticmethod
    def translateXY(xy: str) -> list:
        x = ord(xy[0]) - 97
        y = int(xy[1]) - 1
        if x not in range(0, 8) or y not in range(0, 8):
            raise Exception("Index out of the board")
        return [x, y]

    def __str__(self):
        for row in list(reversed(self.get_board())):
            for cell in row:
                if cell.hasMoved():
                    print(moved, end='')
                if cell.getFigure() is None:
                    if cell.hasMoved():
                        print(' ' + reset, end=' ')
                    else:
                        print(' ', end=' ')
                else:
                    print(cell, end=' ')
                print(reset, end='')
            print()
        print('\n|--------------|')
        return ''

    def isMoveLegal(self, sourceCell: Cell, destinationCell: Cell) -> bool:
        try:
            if sourceCell.getFigure().get_color() == destinationCell.getFigure().get_color():
                return False
        except AttributeError:
            pass

        if sourceCell.getFigure().__class__.__name__ == "Knight" or sourceCell.getFigure().__class__.__name__ == "Pawn":
            if sourceCell.getFigure().isMovePossible(sourceCell, destinationCell):
                return True
            return False

        if sourceCell.getX() == destinationCell.getX():
            if self.checkVertical(sourceCell, destinationCell):
                return True
            return False
        elif sourceCell.getY() == destinationCell.getY():
            if self.checkHorziontal(sourceCell, destinationCell):
                return True
            return False
        else:
            if self.checkDiagonal(sourceCell, destinationCell):
                return True
            return False

    def checkTurn(self, sourceCell: Cell):
        if sourceCell.getFigure().get_color() != self.getTurn():
            raise Exception("Not your turn")

    def checkForCheck(self, turn: str) -> bool:
        king = self.get_king(turn)
        if self.checkVerticalCheck(king) or self.checkHorizontalCheck(king) or self.checkDiagonalCheck(king):
            return True
        return False

    def checkHorizontalCheck(self, king: Cell):
        row = self.get_board()[king.getY()]
        for cell in row:
            if cell.getFigure() is not None and cell.getFigure().isMovePossible(cell, king) and cell is not king:
                return True
        return False

    def checkVerticalCheck(self, king: Cell):
        board = self.get_board()
        x = king.getX()
        for i in range(8):
            cell = board[i][x]
            if cell.getFigure() is not None and cell.getFigure().isMovePossible(cell, king) and cell is not king:
                return True
        return False

    def checkDiagonalCheck(self, king: Cell):
        board = self.get_board()
        x = king.getX()
        y = king.getY()
        while x > 0 and y > 0:
            cell = board[y - 1][x - 1]
            if cell.getFigure() is not None and cell.getFigure().isMovePossible(cell, king):
                return True
            x, y = x - 1, y - 1

        x = king.getX()
        y = king.getY()
        while x < 7 and y < 7:
            cell = board[y + 1][x + 1]
            if cell.getFigure() is not None and cell.getFigure().isMovePossible(cell, king):
                return True
            x, y = x + 1, y + 1

        x = king.getX()
        y = king.getY()
        while x > 0 and y < 7:
            cell = board[y + 1][x - 1]
            if cell.getFigure() is not None and cell.getFigure().isMovePossible(cell, king):
                return True
            x, y = x - 1, y + 1

        x = king.getX()
        y = king.getY()
        while x < 7 and y > 0:
            cell = board[y - 1][x + 1]
            if cell.getFigure() is not None and cell.getFigure().isMovePossible(cell, king):
                return True
            x, y = x + 1, y + 1

        return False

    def checkVertical(self, source: Cell, destination: Cell) -> bool:
        board = self.get_board()
        stop = abs(source.getY() - destination.getY())
        if source.getY() < destination.getY():
            for y in range(stop):
                if board[source.getY() + 1 + y][source.getX()].getFigure() is not None:
                    return False
            return True
        else:
            for y in range(stop):
                if board[source.getY() - 1 - y][source.getX()].getFigure() is not None:
                    return False
            return True

    def checkHorziontal(self, source: Cell, destination: Cell) -> bool:
        board = self.get_board()
        stop = abs(source.getX() - destination.getX())
        if source.getX() < destination.getX():
            for x in range(stop):
                if board[source.getY()][source.getX() + 1 + x].getFigure() is not None:
                    return False
            return True
        else:
            for x in range(stop):
                if board[source.getY()][source.getX() - 1 - x].getFigure() is not None:
                    return False
            return True

    def checkDiagonal(self, source: Cell, destination: Cell) -> bool:
        board = self.get_board()
        stop = abs(source.getX() - destination.getX())
        if source.getX() < destination.getX() and source.getY() < destination.getY():
            for xy in range(stop):
                if board[source.getY() + xy + 1][source.getX() + xy + 1].getFigure() is not None:
                    if board[source.getY() + xy + 1][source.getX() + xy + 1] \
                            .getFigure().get_color() == source.getFigure().get_color():
                        return False
            return True
        elif source.getX() < destination.getX() and source.getY() > destination.getY():
            for xy in range(stop):
                if board[source.getY() - xy - 1][source.getX() + xy + 1].getFigure() is not None:
                    return False
            return True
        elif source.getX() > destination.getX() and source.getY() > destination.getY():
            for xy in range(stop):
                if board[source.getY() - 1 - xy][source.getX() - 1 - xy].getFigure() is not None:
                    return False
            return True
        elif source.getX() > destination.getX() and source.getY() < destination.getY():
            for xy in range(stop):
                if board[source.getY() + 1 + xy][source.getX() - 1 - xy].getFigure() is not None:
                    return False
            return True

    def resetRecentlyMoved(self):
        for cell in self._recentlyMoved:
            cell.set_hasMoved(False)
        self._recentlyMoved.clear()

    def addRecentlyMoved(self, source: Cell, destination: Cell):
        self._recentlyMoved.append(source)
        self._recentlyMoved.append(destination)

    def move(self, source: str, destination: str):
        self.resetRecentlyMoved()
        source = self.translateXY(source)
        destination = self.translateXY(destination)
        sourceCell = self.get_board()[source[1]][source[0]]
        destinationCell = self.get_board()[destination[1]][destination[0]]
        self.checkTurn(sourceCell)
        if not sourceCell.getFigure().isMovePossible(sourceCell, destinationCell) or source == destination:
            raise Exception("Move not possible")
        if not self.isMoveLegal(sourceCell, destinationCell):
            raise Exception("Move not legal")
        # if not self.checkForCheck(self.getTurn()):
        #     raise Exception("There is a check")
        if destinationCell.getFigure() is not None:
            self.capture(sourceCell, destinationCell)
        destinationCell.placeFigure(sourceCell.getFigure())
        destinationCell.set_hasMoved(True)
        sourceCell.removeFigure()
        sourceCell.set_hasMoved(True)
        self.addRecentlyMoved(sourceCell, destinationCell)
        self.changeTurn()
        print(self)

    def capture(self, source: Cell, destination: Cell):
        self.increacePoints(source.getFigure().get_color(), destination.getFigure().get_value())
        print(f"{source.getFigure().get_color()} player: +{destination.getFigure().get_value()} point(s)")
