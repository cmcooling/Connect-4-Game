import random

def height(board):
    heights = []
    for i in board:
        try:
	        height = i.index(0)
	        heights.append(height)
        except ValueError:
            heights.append(6)
    return heights

win_pos = []

for i in range(7):
    for j in range(3):
        pos = []
        pos.append(str(i)+str(j))
        pos.append(str(i)+str(j+1))
        pos.append(str(i)+str(j+2))
        pos.append(str(i)+str(j+3))
        win_pos.append(pos)
for i in range(6):
    for j in range(4):
        pos = []
        pos.append(str(j)+str(i))
        pos.append(str(j+1)+str(i))
        pos.append(str(j+2)+str(i))
        pos.append(str(j+3)+str(i))
for i in range(4):
    for j in range(3):
        pos = []
        pos.append(str(i)+str(j))
        pos.append(str(i+1)+str(j+1))
        pos.append(str(i+2)+str(j+2))
        pos.append(str(i+3)+str(j+3))
        win_pos.append(pos)
for i in range(3,7):
    for j in range(3):
        pos = []
        pos.append(str(i)+str(j))
        pos.append(str(i-1)+str(j+1))
        pos.append(str(i-2)+str(j+2))
        pos.append(str(i-3)+str(j+3))
        win_pos.append(pos)


def winning(board, player_number):
    if board[3][0] == 0:
        return 3
    heights = height(board)
    other_p_number = abs(player_number-3)
    isdanger = False
    isthreepossible = False
    possible_moves = [0,1,2,3,4,5,6,7]
    for i in win_pos:
        pieces = [board[int(i[x][0])][int(i[x][1])] for x in range(4)]
        if pieces.count(player_number) == 3 and pieces.count(0) == 1:
            missing = i[pieces.index(0)]
            if int(missing[1]) == heights[int(missing[0])]:
                return int(missing[0])
        elif pieces.count(other_p_number) == 3 and pieces.count(0) == 1:
            missing = i[pieces.index(0)]
            if int(missing[1]) == heights[int(missing[0])]:
                danger = int(missing[0])
                isdanger = True
            elif int(missing[1]) == heights[int(missing[0])]+1:
                bad = int(missing[0])
                possible_moves.remove(bad)
        elif pieces.count(player_number) == 2 and pieces.count(0) == 2:
            ii = [i for i, x in enumerate(pieces) if x == 0]
            missing1 = i[ii[0]]
            missing2 = i[ii[1]]
            if int(missing1[1]) == heights[int(missing1[0])] and int(missing2[1]) == heights[int(missing2[0])]:
                missing = [int(missing1[0]),int(missing2[0])]	        
                next_best = min(missing, key=lambda x:abs(x-3))
                isthreepossible = True
            elif int(missing1[1]) == heights[int(missing1[0])]:
                next_best = int(missing1[0])
                isthreepossible = True
            elif int(missing2[1]) == heights[int(missing2[0])]: 
                next_best = int(missing2[0])
                isthreepossible = True
    if isdanger is True:
        return danger
    elif isthreepossible is True:    
        return next_best
    else:
        return random.choice(possible_moves)
    
    