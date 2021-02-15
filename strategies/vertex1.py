import random


def vertex(board, player_number):
    vertex1return = vertex1(board, player_number)
    if type(vertex1return) != int or vertex1return < 0 or vertex1return > 6:
        return random_move(board)
    return vertex1return


def vertex1(board, player_number):

    try:
        # SET THE PLAYER TO SELF OR OTHER
        if player_number == 1:
            us = 1
            them = 2
        elif player_number == 2:
            us = 2
            them = 1

        # check if i'm starting
        if start_move(board, us, them) != None:
            return start_move(board, us, them)

        # CHECK IF I HAVE A LINE OF 3 AND I CAN WIN
        elif check_win_move(board, us, them) != None:
            return check_win_move(board, us, them)

        # BLOCK OPPONENT IF THEY HAVE A LINE OF 3
        elif check_opponent_win_move(board, us, them) != None:
            return check_opponent_win_move(board, us, them)

        # BLOCK A SNEAKY OPEN-END DOUBLE
        elif check_horizontal_double(board, us, them) != None:
            return check_horizontal_double(board, us, them)

        # CHECK FOR MY LINES OF 2
        elif find_2inline(board, us, them) != None:
            return find_2inline(board, us, them)

        # CHECK FOR MY SINGLES
        # randomly choose 1 and build on it

        elif find_one(board, us, them) != None:
            return find_one(board, us, them)

        else:
            return random_move(board)

    except:
        return random_move(board)

# MAKE RANDOM MOVE BUT DON'T OVERFILL


def random_move(board):
    full_column = True
    while full_column:
        attempt = random.randint(0, 6)
        if board[attempt][5] == 0:
            full_column = False
    return attempt


# START MOVE


def start_move(board, us, them):
    blanker = 0
    for col in range(7):
        if board[col][0] == 0:
            blanker = blanker + 1
    if blanker == 7:
        return 3
    else:
        return None


# FUNCTIONS FOR LINES OF 3


def check_columns_3inline(board, us, them):
    for col in range(7):
        column = board[col]
        for row in range(3):
            if column[row] == them and column[row + 1] == them and column[row + 2] == them:
                if column[row + 3] != us:
                    return col


def check_rows_3inline(board, us, them):
    for row in range(6):
        for col in range(5):
            if board[col][row] == them and board[col + 1][row] == them and board[col + 2][row] == them:
                if col == 0:
                    if board[col + 3][row] != us:
                        if row == 0 or board[col + 3][row - 1] != 0:
                            return (col + 3)
                elif col == 4:
                    if board[col - 1][row] != us:
                        if row == 0 or board[col - 1][row - 1] != 0:
                            return (col - 1)
                else:
                    if board[col - 1][row] != us:
                        if board[col + 3][row] != us:
                            if row == 0:
                                if col < 3:
                                    return (col + 3)
                                else:
                                    return (col - 1)
                            elif board[col - 1][row - 1] != 0:
                                if board[col + 3][row - 1] != 0:
                                    if col < 3:
                                        return (col + 3)
                                    else:
                                        return (col - 1)
                                else:
                                    return (col - 1)
                            elif board[col + 3][row - 1] != 0:
                                return (col + 3)
                        else:
                            if board[col - 1][row - 1] != 0 or row == 0:
                                return (col - 1)
                    elif board[col + 3][row] != us:
                        if board[col + 3][row - 1] != 0 or row == 0:
                            return (col + 3)


def check_positive_diagonal_3inline(board, us, them):
    for row in range(4):
        for col in range(5):
            if board[col][row] == them and board[col + 1][row + 1] == them and board[col + 2][row + 2] == them:
                if row == 0 and col != 4:
                    if board[col + 3][row + 3] != us:
                        if board[col + 3][row + 2] != 0:
                            return (col + 3)
                elif row < 3 and col != 4:
                    if board[col - 1][row - 1] != us:
                        if board[col - 1][row - 2] != 0 or row == 1:
                            return (col - 1)
                    elif board[col + 3][row + 3] != us:
                        if board[col + 3][row + 2] != 0:
                            return (col + 3)
                elif row == 3:
                    if col != 0 and board[col - 1][row - 1] != us:
                        if board[col - 1][row - 2] != 0:
                            return (col - 1)


def check_positive_diagonal_gap(board, us, them):
    for row in range(3):
        for col in range(4):
            if board[col][row] == them and board[col + 1][row + 1] == them and board[col + 3][row + 3] == them:
                if board[col + 2][row + 2] != us:
                    if board[col + 2][row + 1] != 0:
                        return (col + 2)
            if board[col][row] == them and board[col + 2][row + 2] == them and board[col + 3][row + 3] == them:
                if board[col + 1][row + 1] != us:
                    if board[col + 1][row] != 0:
                        return (col + 1)


def check_negative_diagonal_3inline(board, us, them):
    for row in range(4):
        for col in range(6, 1, -1):
            if board[col][row] == them and board[col - 1][row + 1] == them and board[col - 2][row + 2] == them:
                if row == 0 and col != 2:
                    if board[col - 3][row + 3] != us:
                        if board[col - 3][row + 2] != 0:
                            return (col - 3)
                elif row < 3:
                    if col != 6 and board[col + 1][row - 1] != us:
                        if row == 1 or board[col + 1][row - 2] != 0:
                            return (col + 1)
                    elif col != 2 and board[col - 3][row + 3] != us:
                        if board[col - 3][row + 2] != 0:
                            return (col - 3)
                elif row == 3:
                    if col != 6 and board[col + 1][row - 1] != us:
                        if board[col + 1][row - 2] != 0:
                            return (col + 1)


def check_negative_diagonal_gap(board, us, them):
    for row in range(3):
        for col in range(6, 2, -1):
            if board[col][row] == them and board[col - 1][row + 1] == them and board[col - 3][row + 3] == them:
                if board[col - 2][row + 2] != us:
                    if board[col - 2][row + 1] != 0:
                        return (col - 2)
            if board[col][row] == them and board[col - 2][row + 2] == them and board[col - 3][row + 3] == them:
                if board[col - 1][row + 1] != us:
                    if board[col - 1][row] != 0:
                        return (col - 1)


def check_horizontal_gap(board, us, them):
    for row in range(6):
        for col in range(4):
            if board[col][row] == them and board[col + 1][row] == them and board[col + 3][row] == them:
                if board[col + 2][row] != us:
                    if row == 0 or board[col + 2][row - 1] != 0:
                        return (col + 2)
        for col in range(6, 2, -1):
            if board[col][row] == them and board[col - 1][row] == them and board[col - 3][row] == them:
                if board[col - 2][row] != us:
                    if row == 0 or board[col - 2][row - 1] != 0:
                        return (col - 2)

# HORIZONTAL DOUBLE STRATEGY


def check_horizontal_double(board, us, them):
    for row in range(6):
        for col in range(1, 5):
            if board[col][row] == them and board[col + 1][row] == them:
                if board[col - 1][row] != us and board[col + 2][row] != us:
                    if col == 1 or col == 2:
                        return (col + 2)
                    elif col == 3 or col == 4:
                        return (col - 1)

# WINNING MOVES JOINING LINE OF 3 FUNCTIONS


def check_opponent_win_move(board, us, them):
    if check_columns_3inline(board, us, them) != None:
        return check_columns_3inline(board, us, them)
    elif check_rows_3inline(board, us, them) != None:
        return check_rows_3inline(board, us, them)
    elif check_horizontal_gap(board, us, them) != None:
        return check_horizontal_gap(board, us, them)
    elif check_positive_diagonal_3inline(board, us, them) != None:
        return check_positive_diagonal_3inline(board, us, them)
    elif check_negative_diagonal_3inline(board, us, them) != None:
        return check_negative_diagonal_3inline(board, us, them)
    elif check_positive_diagonal_gap(board, us, them) != None:
        return check_positive_diagonal_gap(board, us, them)
    elif check_negative_diagonal_gap(board, us, them) != None:
        return check_negative_diagonal_gap(board, us, them)


def check_win_move(board, us, them):
    # us and them
    quisling = us
    us = them
    them = quisling
    if check_opponent_win_move(board, us, them) != None:
        return check_opponent_win_move(board, us, them)
    else:
        return None


# FIND MY LINE OF 2

def find_column_of_2(board, us, them):
    for col in range(7):
        for row in range(3, 0, -1):
            if board[col][row] == us and board[col][row - 1] == us:
                if board[col][row + 1] == 0:
                    return col


def find_row_of_2(board, us, them):
    for row in range(5, -1, -1):
        for col in range(6):
            if board[col][row] == us and board[col + 1][row] == us:
                if col < 4:
                    if board[col + 2][row] == 0 and board[col + 3][row] == 0:
                        if row == 0 or board[col + 2][row - 1] != 0:
                            return (col + 2)
                    elif board[col - 1][row] == 0 and board[col + 2][row] == 0:
                        if row == 0 or board[col - 1][row - 1] != 0:
                            return (col - 1)
                        elif board[col + 2][row - 1] != 0:
                            return (col + 2)
                    elif board[col - 1][row] == 0 and board[col - 2][row] == 0:
                        if row == 0 or board[col - 1][row - 1] != 0:
                            return (col - 1)
                elif col == 4:
                    if board[col - 1][row] == 0 and board[col + 2][row] == 0:
                        if row == 0 or board[col - 1][row - 1] != 0:
                            return (col - 1)
                        elif board[col + 2][row - 1] != 0:
                            return (col + 2)
                elif col == 5:
                    if board[col - 1][row] == 0 and board[col - 2][row] == 0:
                        if row == 0 or board[col - 1][row - 1] != 0:
                            return (col - 1)


def find_2inline(board, us, them):
    if find_column_of_2(board, us, them) != None:
        return find_column_of_2(board, us, them)
    if find_row_of_2(board, us, them) != None:
        return find_row_of_2(board, us, them)

# FIND 1 TO BUILD ON


def find_one(board, us, them):
    for row in range(3):
        for col in range(7):
            if board[col][row] == us:
                if board[col][row + 1] == 0:
                    return (col)
