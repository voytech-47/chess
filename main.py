from pprint import pprint

from Components.Board import *

board = Borad()
board.placeFigures()

print(board)

board.move("e1", "f2")
board.move("d8", 'a5')
board.move("f2", "f3")
board.move("a5", 'b2')
# board.move("f8", "b4")  # [5, 7], [1, 3]

# print(board)
# print(board.translateXY("e2"))
