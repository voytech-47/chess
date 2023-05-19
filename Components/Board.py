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

    def __init__(self):
        for x in range(8):
            for y in range(8):
                cell = Cell(x, y)
                self.board[y].append(cell)

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
        blackKing = King('black')
        self.board[-1][4].placeFigure(blackKing)

    def get_board(self):
        return self.board

    def changeTurn(self):
        self.turn = (self.turn + 1) % 2

    def getTurn(self):
        if self.turn:
            return "black"
        return "white"

    @staticmethod
    def translateXY(xy):
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

    def isMoveLegal(self, sourceCell, destinationCell):
        try:
            if sourceCell.getFigure().get_color() == destinationCell.getFigure().get_color():
                return False
        except AttributeError:
            pass
        if sourceCell.getFigure().__class__.__name__ == "Knight":
            return True

        board = self.get_board()

        # when moving vertically
        if sourceCell.getX() == destinationCell.getX():
            stop = abs(sourceCell.getY() - destinationCell.getY())
            if sourceCell.getY() < destinationCell.getY():
                for y in range(stop):
                    if board[sourceCell.getY() + 1 + y][sourceCell.getX()].getFigure() is not None:
                        return False
                return True
            else:
                for y in range(stop):
                    if board[sourceCell.getY() - 1 - y][sourceCell.getX()].getFigure() is not None:
                        return False
                return True

        # when moving vertically
        elif sourceCell.getY() == destinationCell.getY():
            stop = abs(sourceCell.getX() - destinationCell.getX())
            if sourceCell.getX() < destinationCell.getX():
                for x in range(stop):
                    if board[sourceCell.getY()][sourceCell.getX() + 1 + x].getFigure() is not None:
                        return False
                return True
            else:
                for x in range(stop):
                    if board[sourceCell.getY()][sourceCell.getX() - 1 - x].getFigure() is not None:
                        return False
                return True

        # when moving diagonally
        else:
            stop = abs(sourceCell.getX() - destinationCell.getX())
            if sourceCell.getX() < destinationCell.getX() and sourceCell.getY() < destinationCell.getY():
                for xy in range(stop):
                    if board[sourceCell.getY() + xy + 1][sourceCell.getX() + xy + 1].getFigure() is not None:
                        if board[sourceCell.getY() + xy + 1][sourceCell.getX() + xy + 1]\
                                .getFigure().get_color() == sourceCell.getFigure().get_color():
                            return False
                return True
            elif sourceCell.getX() < destinationCell.getX() and sourceCell.getY() > destinationCell.getY():
                for xy in range(stop):
                    if board[sourceCell.getY() - xy - 1][sourceCell.getX() + xy + 1].getFigure() is not None:
                        return False
                return True
            elif sourceCell.getX() > destinationCell.getX() and sourceCell.getY() > destinationCell.getY():
                for xy in range(stop):
                    if board[sourceCell.getY() - 1 - xy][sourceCell.getX() - 1 - xy].getFigure() is not None:
                        return False
                return True
            elif sourceCell.getX() > destinationCell.getX() and sourceCell.getY() < destinationCell.getY():
                for xy in range(stop):
                    if board[sourceCell.getY() + 1 + xy][sourceCell.getX() - 1 - xy].getFigure() is not None:
                        return False
                return True

    def checkTurn(self, sourceCell):
        if sourceCell.getFigure().get_color() != self.getTurn():
            raise Exception("Not your turn")

    def resetRecentlyMoved(self):
        for cell in self._recentlyMoved:
            cell.set_hasMoved(False)
        self._recentlyMoved.clear()

    def addRecentlyMoved(self, source, destination):
        self._recentlyMoved.append(source)
        self._recentlyMoved.append(destination)

    def move(self, source, destination):
        self.resetRecentlyMoved()
        source = self.translateXY(source)
        destination = self.translateXY(destination)
        sourceCell = self.get_board()[source[1]][source[0]]
        destinationCell = self.get_board()[destination[1]][destination[0]]
        self.checkTurn(sourceCell)
        if not sourceCell.getFigure().isMovePossible(source, destination) or source == destination:
            raise Exception("Move not possible")
        if not self.isMoveLegal(sourceCell, destinationCell):
            raise Exception("Move not legal")
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
        print(f"{source.getFigure().get_color()} player: +{destination.getFigure().get_value()} points")
