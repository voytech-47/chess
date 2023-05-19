from pprint import pprint

from Components.Board import *

from colored import bg, fg, attr

green = bg('indian_red_1a') + fg('green')
reset = attr('reset')

board = Borad()
board.placeFigures()

print(board)

board.move("d2", "d3")
board.move("h7", "h6")
board.move("c1", "h6")
# board.move("b8", "c6")
# board.move("c2", "c4")
# board.move("g8", "f6")
# board.move("f1", "d3")
# board.move("f8", "b4")
# board.move("g1", "f3")
# board.move("d7", "d6")
# board.move("b1", "c3")
# board.move("c8", "g4")
# board.move("c1", "g5")
# board.move("h7", "h6")
# board.move("g5", "h4")
# board.move("e8", "f8")

# print('print'+reset+'after')

# board.move("f8", "b4")  # [5, 7], [1, 3]

# print(board)
# print(board.translateXY("e2"))
