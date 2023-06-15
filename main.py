from pprint import pprint

from Components.Board import *

from colored import bg, fg, attr

green = bg('indian_red_1a') + fg('green')
reset = attr('reset')

board = Board()
board.place_figures()

print(board)

board.move("d2", "d3")
board.move("e7", "e6")
board.move("h2", "h4")
print(board.check_diagonal_check(board.get_king(board.get_turn())))
print(board.check_vertical_check(board.get_king(board.get_turn())))
print(board.check_horizontal_check(board.get_king(board.get_turn())))
print(board.check_for_check(board.get_turn()))
board.move("f8", "b4")
print(board.check_diagonal_check(board.get_king(board.get_turn())))
print(board.check_for_check(board.get_turn()))
# board.move("e2", "e4")
# board.move("e7", "e5")
# board.move("d2", "d4")
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

# print('print'+reset_background+'after')

# board.move("f8", "b4")  # [5, 7], [1, 3]

# print(board)
# print(board.translateXY("e2"))
