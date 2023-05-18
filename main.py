from pprint import pprint

from Components.Board import *

board = Borad()
board.placeFigures()

print(board)
board.move("e2", "e4")
board.move("e7", 'e5')
board.move("g1", "f3")
# print(board)
# print(board.translateXY("e2"))