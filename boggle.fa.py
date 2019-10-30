import random

# When the board is empty, you will print out
# board = [
#     ['A', '_', '_', '_'],
#     ['_', 'B', '_', '_'],
#     ['_', '_', 'C', '_'],
#     ['_', '_', '_', 'D']
# ]

# for row in board:
#     print(row)

# for dx, dy in board:
#     print(dx)

# print('\n'.join([str(row) for row in board]))

# create a 4x4 board with 16 characters and print it out, for example:

# you can run your algorithm again and make sure every "shake" will create a new set of characters

# create a list of strings, 16 in total
list_of_strings = [
    ['A', 'A', 'E', 'E', 'G', 'N'],
    ['E', 'L', 'R', 'T', 'T', 'Y'],
    ['A', 'O', 'O', 'T', 'T', 'W'],
    ['A', 'B', 'B', 'J', 'O', 'O'],
    ['E', 'H', 'R', 'T', 'V', 'W'],
    ['C', 'I', 'M', 'O', 'T', 'U'],
    ['D', 'I', 'S', 'T', 'T', 'Y'],
    ['E', 'I', 'O', 'S', 'S', 'T'],
    ['D', 'E', 'L', 'R', 'V', 'Y'],
    ['A', 'C', 'H', 'O', 'P', 'S'],
    ['H', 'I', 'M', 'N', 'Q', 'U'],
    ['E', 'E', 'I', 'N', 'S', 'U'],
    ['E', 'E', 'G', 'H', 'N', 'W'],
    ['A', 'F', 'F', 'K', 'P', 'S'],
    ['H', 'L', 'N', 'N', 'R', 'Z'],
    ['D', 'E', 'I', 'L', 'R', 'X']
]

dummy_board = []


def display_board(any_board):
    print('[' + any_board[0] + ',' + any_board[1] +
          ',' + any_board[2] + ',' + any_board[3] + ']')
    print('[' + any_board[4] + ',' + any_board[5] +
          ',' + any_board[6] + ',' + any_board[7] + ']')
    print('[' + any_board[8] + ',' + any_board[9] +
          ',' + any_board[10] + ',' + any_board[11] + ']')
    print('[' + any_board[12] + ',' + any_board[13] +
          ',' + any_board[14] + ',' + any_board[15] + ']')


for dice in list_of_strings:
    dummy_board.append(random.choice(dice))
# print(dummy_board)

display_board(dummy_board)


# for y, row in enumerate(board, 1):
#     print(y, row)
#     for x, cell in enumerate(row, 1):
#         print(x, cell)
