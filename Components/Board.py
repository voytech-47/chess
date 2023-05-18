from Components.Cell import Cell
from Figures.Bishop import Bishop
from Figures.King import King
from Figures.Knight import Knight
from Figures.Pawn import Pawn
from Figures.Queen import Queen
from Figures.Rook import Rook


class Borad:
    board = [[] for i in range(8)]

    def __init__(self):
        for x in range(8):
            for y in range(8):
                cell = Cell(x, y)
                self.board[y].append(cell)

    def placeFigures(self):
        for y in range(8):
            whitePawn = Pawn('black')
            self.board[1][y].placeFigure(whitePawn)
            blackPawn = Pawn('white')
            self.board[-2][y].placeFigure(blackPawn)

        for y in range(0, 8, 7):
            whiteRook = Rook('black')
            self.board[0][y].placeFigure(whiteRook)
            blackRook = Rook('white')
            self.board[-1][y].placeFigure(blackRook)

        for y in range(1, 7, 5):
            whiteKnight = Knight('black')
            self.board[0][y].placeFigure(whiteKnight)
            blackKnight = Knight('white')
            self.board[-1][y].placeFigure(blackKnight)

        for y in range(2, 6, 3):
            whiteBishop = Bishop('black')
            self.board[0][y].placeFigure(whiteBishop)
            blackBishop = Bishop('white')
            self.board[-1][y].placeFigure(blackBishop)

        whiteQueen = Queen('black')
        self.board[0][3].placeFigure(whiteQueen)
        blackQueen = Queen('white')
        self.board[-1][3].placeFigure(blackQueen)
        whiteKing = King('black')
        self.board[0][4].placeFigure(whiteKing)
        blackKing = King('white')
        self.board[-1][4].placeFigure(blackKing)

    def get_board(self):
        return self.board

    @staticmethod
    def translateXY(xy):
        x = ord(xy[0]) - 97
        y = int(xy[1]) - 1
        if x not in range(0, 8) or y not in range(0, 8):
            raise Exception("Index out of the board")
        return f"{x}{y}"

    def __str__(self):
        for row in self.get_board():
            print([str(cell) for cell in row])
        return ''
