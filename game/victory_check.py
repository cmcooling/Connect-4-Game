'''This module contains files for checking if a board state is a victory for either player'''


def check_column_victory(column):
    '''Checks a single column for a vertical victory
    (param) column ([int]*6): A column of the board
    (return) Will be 0 for no win, 1 for player 1 win, or 2 for player 2 win'''
    for i_start in range(3):
        start_owner = column[i_start]
        if start_owner == 0:
            continue

        for i_next in range(i_start, i_start + 4):
            if column[i_next] != start_owner:
                break
        else:
            return start_owner

    return 0


def check_vertical_victory(board):
    '''Checks an entire board for a vertical victory
    (param) board ([[int]*6]*7): A board
    (return) Will be 0 for no win, 1 for player 1 win, or 2 for player 2 win'''
    for column in board:
        column_victory = check_column_victory(column)
        if column_victory:
            return column_victory


def check_horizontal_victory(board):
    '''Checks an entire board for a horizontal victory
    (param) board ([[int]*6]*7): A board
    (return) Will be 0 for no win, 1 for player 1 win, or 2 for player 2 win'''
    for i_row in range(6):
        for i_start in range(4):
            start_owner = board[i_start][i_row]

            if not start_owner:
                continue

            for i_next in range(i_start, i_start + 4):
                if board[i_next][i_row] != start_owner:
                    break
            else:
                return start_owner

    return 0


def check_positive_diagonal_victory(board):
    '''Checks an entire board for a diagonal victory running bottom-left to top-right
    (param) board ([[int]*6]*7): A board
    (return) Will be 0 for no win, 1 for player 1 win, or 2 for player 2 win'''
    for i_row_start in range(3):
        for i_column_start in range(4):
            start_owner = board[i_column_start][i_row_start]

            if not start_owner:
                continue

            for i in range(4):
                if board[i_column_start + i][i_row_start + i] != start_owner:
                    break
            else:
                return start_owner

    return 0


def check_negative_diagonal_victory(board):
    '''Checks an entire board for a diagonal victory running top-left to bottom-right
    (param) board ([[int]*6]*7): A board
    (return) Will be 0 for no win, 1 for player 1 win, or 2 for player 2 win'''
    for i_row_start in range(3, 6):
        for i_column_start in range(4):
            start_owner = board[i_column_start][i_row_start]

            if not start_owner:
                continue

            for i in range(4):
                if board[i_column_start + i][i_row_start - i] != start_owner:
                    break
            else:
                return start_owner

    return 0


def check_draw(board):
    '''Checks if the game ended in a draw'''
    for column in board:
        if min(column) == 0:
            return 0
    else:
        return -1


def check_victory(board):
    '''Checks an entire board for any type of victory
    (param) board ([[int]*6]*7): A board
    (return) Will be 0 for no win, 1 for player 1 win, or 2 for player 2 win'''
    victory = check_vertical_victory(board)
    if victory:
        return victory

    victory = check_horizontal_victory(board)
    if victory:
        return victory

    victory = check_positive_diagonal_victory(board)
    if victory:
        return victory

    victory = check_negative_diagonal_victory(board)
    if victory:
        return victory

    victory = check_draw(board)
    if victory:
        return victory

    return 0
