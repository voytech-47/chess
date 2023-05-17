from Bishop import Bishop
from King import King
from Knight import Knight
from Queen import Queen
from Rook import Rook
from Pawn import Pawn
from Cell import Cell


class Borad:
    board = [[] for i in range(8)]

    def __init__(self):
        for y in range(8):
            for x in range(8):
                cell = Cell(x, y)
                self.board[x].append(cell)

    def placeFigures(self):
        for x in range(8):
            whitePawn = Pawn('white')
            self.board[1][x].placeFigure(whitePawn)
            blackPawn = Pawn('black')
            self.board[-2][x].placeFigure(blackPawn)

        for x in range(0, 8, 7):
            whiteRook = Rook('white')
            self.board[0][x].placeFigure(whiteRook)
            blackRook = Rook('black')
            self.board[-1][x].placeFigure(blackRook)

        for x in range(1, 7, 6):
            whiteKnight = Knight('white')
            self.board[0][x].placeFigure(whiteKnight)
            blackKnight = Knight('black')
            self.board[-1][x].placeFigure(blackKnight)

        for x in range(2, 6, 5):
            whiteBishop = Bishop('white')
            self.board[0][x].placeFigure(whiteBishop)
            blackBishop = Bishop('black')
            self.board[-1][x].placeFigure(blackBishop)

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

    # def __str__(self):
    #     print(self.get_board())
    #     return ''
