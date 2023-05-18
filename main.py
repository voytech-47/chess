from pprint import pprint

from Components.Board import *

board = Borad()
board.placeFigures()

print(board)
board.move("e2", "e4")
print(board)
# print(board.translateXY("e2"))

