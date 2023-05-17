from Board import *

board = Borad()
board.placeFigures()
board = board.get_board()

for row in board:
    print([str(cell) for cell in row])
