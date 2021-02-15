import random

COL_COUNT= 7
ROW_COUNT=6
PLAYER_PIECE=1
AI_PIECE=2
WINDOW_LENGTH=4
EMPTY=0


def drop_piece(board, col ,row, piece):
    nboard=board.copy()
    nboard[col][row]=piece
    return nboard
def remove_piece(board,col,row):
    board[col][row]=0
    return board
def get_next_open_row(board, col):
    col_list=board[col]
    for i in range(len(col_list)):
        if col_list[i]==0:
            return i

def is_valid_location(board, col):
	return board[col][5] == 0


def get_valid_locations(board):
    valid_location = []
    for col in range(COL_COUNT):
        if is_valid_location(board,col):
            valid_location.append(col)

    return valid_location

def evaluate_window(window,piece):
    score=0
    opponent_piece=1
    if piece==1:
        opponent_piece=2
    else:
         opponent_piece=1


    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(0)==2:
        score+=5
    if window.count(opponent_piece)==3 and window.count(0)==1:
        score-=20


    return score



def score_position(board,piece):
    ##horizontal score
    score=0
    center_array = board[COL_COUNT//2]
    center_count = center_array.count(piece)
    score+=center_count*3

    for r in range(ROW_COUNT):
        row_array=  [int(board[i][r]) for i in range(COL_COUNT)]
        for c in range(COL_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score+=evaluate_window(window,piece)

    for c in range(COL_COUNT):
        col_array= board[c]
        for i in range(ROW_COUNT-3):
            window = col_array[i:i+WINDOW_LENGTH]
            score+=evaluate_window(window,piece)
   
    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT-3):
            window = [board[c+i][r+i] for i in range(WINDOW_LENGTH)]
            score+=evaluate_window(window,piece)

    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT-3):
            window = [board[c+i][r+3-i] for i in range(WINDOW_LENGTH)]
            score+=evaluate_window(window,piece)

    
    return score


def pick_best_move(board,piece):
    best_score=-1800
    valid_locations= get_valid_locations(board)
    best_col= random.choice(valid_locations)
    board= board.copy()

    for col in valid_locations:
        temp_board = board.copy()
        row = get_next_open_row(temp_board,col)
        board=drop_piece(temp_board,col,row,piece)
        score = score_position(board,piece)
        

        if score>best_score:
            best_score=score
            best_col=col

        remove_piece(board,col,row)

    return best_col


