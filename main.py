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
                return (row, column)
