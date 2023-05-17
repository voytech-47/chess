import Bishop
import King
import Knight
import Pawn
import Queen
from Rook import Rook


class Borad:
    board = [[] for i in range(8)]

    def __init__(self):
        for y in range(4):
            for x in range(8):
                self.board[x].append(Rook(0, 'w'))
