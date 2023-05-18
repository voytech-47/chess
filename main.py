from pprint import pprint

from Components.Board import *

board = Borad()
board.placeFigures()

print(board)

# board.move("c2", "c3")
# board.move("e7", 'e6')
# board.move("d1", 'b3')
# board.move("e6", 'e5')
# board.move("b3", 'a3')

# board.move("e2", "e4")  # White moves e2 to e4
# board.move("e7", "e5")  # Black moves e7 to e5
# board.move("g1", "f3")  # White moves g1 to f3
# board.move("b8", "c6")  # Black moves b8 to c6
# board.move("f1", "c4")  # White moves f1 to c4

board.move("c2", "c4")  # White's first move: c2 to c4
board.move("e7", "e5")  # Black's first move

board.move("g1", "f3")  # White's second move: g1 to f3
board.move("b8", "c6")  # Black's second move

board.move("f1", "b5")  # White's third move: f1 to b5 (Ruy Lopez)
board.move("a7", "a6")  # Black's third move

board.move("b5", "a4")  # White's fourth move: b5 to a4
board.move("g8", "f6")  # Black's fourth move

board.move("e1", "g1")  # White's fifth move: Castling kingside
board.move("d7", "d6")  # Black's fifth move

board.move("d2", "d4")  # White's sixth move: d2 to d4
board.move("e5", "d4")  # Black's sixth move

# board.move("f8", "b4")  # [5, 7], [1, 3]

# print(board)
# print(board.translateXY("e2"))
