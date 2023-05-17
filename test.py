from pprint import pprint
from Rook import Rook

# table = [8 * [''], 8 * [], 8 * [''], 8 * [''], 8 * [''], 8 * [''], 8 * ['p'], 8 * ['']]

# table = [8 * [8 * []]]
# for i, row in enumerate(table):
#     row.append(i)
#     print(row)

table = [[x+1 for x in range(8)] for y in range(8)]

print(table[0])

# def init(toDict, color, id):
#     major_figures = {
#         0: Rook(color, id),
#         7: 'r',
#         1: 'k',
#         6: 'k',
#         2: 'b',
#         5: 'b',
#         3: 'Q',
#         4: 'K'
#     }
#     return major_figures[toDict]
#
#
# # kon = Rook(0, 0)
#
# # print(kon.value)
#
# for i in range(0, 8):
#     table[i] = init(i, 0, i)
#
# # table[0] = major_figures[0]
#
# pprint(table)
#
# print(table[0].piece_id)
#
# # print(table[0][1])
