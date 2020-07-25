def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        r, c = find

    for row in range(1, 10):
        if valid(board, row, (r, c)):
            board[r][c] = row

            if solve(board):
                return True

            board[r][c] = 0

    return False


def valid(board, num, position):
    # Check row
    for row in range(len(board[0])):
        if board[position[0]][row] == num and position[1] != row:
            return False

    # Check Column
    for row in range(len(board)):
        if board[row][position[1]] == num and position[0] != row:
            return False

    # Check Box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for row in range(box_y * 3, box_y * 3 + 3):
        for column in range(box_x * 3, box_x * 3 + 3):
            if board[row][column] == num and (row, column) != position:
                return False

    return True


def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - -")

            for column in range(len(board[0])):
                if column % 3 == 0 and column != 0:
                    print(" | ", end="")

                if column == 8:
                    print(board[row][column])
                else:
                    print(str(board[row][column]) + " ", end="")


def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return row, column
    return None
