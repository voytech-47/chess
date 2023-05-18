from Components.Cell import Cell
from Figures.Bishop import Bishop
from Figures.King import King
from Figures.Knight import Knight
from Figures.Pawn import Pawn
from Figures.Queen import Queen
from Figures.Rook import Rook


class Borad:
    board = [[] for i in range(8)]
    # turn = 0 -> white, turn = 1 -> black
    turn = 0

    def __init__(self):
        for x in range(8):
            for y in range(8):
                cell = Cell(x, y)
                self.board[y].append(cell)

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
            print([str(cell) for cell in row])
        print(f"Turn: {self.getTurn()}")
        return ''

    def move(self, source, destination):
        source = self.translateXY(source)
        destination = self.translateXY(destination)
        sourceCell = self.get_board()[source[1]][source[0]]
        if not sourceCell.getFigure().isMoveLegal(source, destination):
            raise Exception("Illegal move")
        destinationCell = self.get_board()[destination[1]][destination[0]]
        destinationCell.placeFigure(sourceCell.getFigure())
        sourceCell.removeFigure()
        self.changeTurn()
