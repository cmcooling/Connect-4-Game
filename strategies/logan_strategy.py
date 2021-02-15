import random


def strategy(board, player_number):
    full = []
    column_counter = 0
    for column in board:
        if column[5] != 0:
            full.append(column_counter)
        column_counter += 1
    move = random.randint(0, 6)
    column_counter = 0
    for column in board:
        column_victory = 0
        for i_start in range(3):
            start_owner = column[i_start]
            if start_owner == 0:
                continue
            for i_next in range(i_start, i_start + 3):
                if column[i_next] != start_owner:
                    break
            else:
                column_victory = start_owner
        if column_victory:
            if full.count(column_counter) == 0:
                move = column_counter
        column_counter += 1
    column_counter = 0
    for i_row in range(6):
        for i_start in range(4):
            start_owner = board[i_start][i_row]
            if not start_owner:
                continue
            for i_next in range(i_start, i_start + 3):
                if board[i_next][i_row] != start_owner:
                    break
            else:
                column_counter = [i_start - 1, i_start + 3, i_row]
    if column_counter != 0:
        row_counter = column_counter[len(column_counter)-1]
        column_counter = column_counter[0:len(column_counter)-1]
        column_counter_copy = column_counter
        for i in column_counter_copy:
            if full.count(i) != 0:
                column_counter.remove(i)
            if i < 0 or i > 6:
                column_counter.remove(i)
            if board[i][row_counter] != 0:
                column_counter.remove(i)
            if row_counter != 0:
                if board[i][row_counter-1] != 0:
                    column_counter.remove(i)
        if len(column_counter) == 1:
            move = column_counter[0]
        elif len(column_counter) == 2:
            move = random.choice(column_counter)
    while full.count(move) == 1:
        move = random.randint(0, 6)
    return move



















