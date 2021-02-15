#python 3.8+ is required to run this
#use sterge_tactic_variable_depth.sterge
#Variable Depth version
#depth threshhold may have to be reduced
from copy import deepcopy
from threading import Thread
start = 0
def to_key(state):
    return tuple([x for y in state for x in y])
def sgn(x):
    if x == 0:
        return 0
    return 1 if abs(x) == x else -1
def checkHoriz(b,c,player):
    x = c[0]
    cnc = 1
    for i in range(x - 1 , -1, -1):
        if b[i][c[1]] != player:
            break
        else:
            cnc += 1
    for i in range(x+1, 7):
        if b[i][c[1]] != player:
            break
        else:
            cnc += 1
    if cnc >= 4:
        return player
    else:
        return 0
def checkVert(b,c,player):
    y = c[1]
    if y<3:
        return 0
    cnc = 1
    for i in range(y - 1 , -1, -1):
        if b[c[0]][i] != player:
            break
        else:
            cnc += 1
    if cnc >= 4:
        return player
    else:
        return 0
def checkDiagPos(b,c,player):
    y = c[1]
    x = c[0]
    ih = y-x
    if not (-3 <= ih <= 2):
        return 0
    
    cnc = 1
    for i in range(x - 1, -1, -1):
        if (ih + i) <0:
            break
        if b[i][ih + i] != player:
            break
        else:
            cnc += 1
    for i in range(x+1,7):
        if (ih+i) > 5:
            break
        if b[i][ih + i] != player:
            break
        else:
            cnc += 1
    if cnc >= 4:
        return player
    else:
        return 0
def checkDiagNeg(b,c,player):
    y = c[1]
    x = c[0]
    ih = y+x
    if not(3 <= ih <= 8):
        return 0
    cnc = 1
    for i in range(x - 1, -1, -1):
        if (ih - i) >5:
            break
        if b[i][ih - i] != player:
            break
        else:
            cnc += 1
    for i in range(x+1,7):
        if (ih - i) <0:
            break
        if b[i][ih - i] != player:
            break
        else:
            cnc += 1
    if cnc >= 4:
        return player
    else:
        return 0
def checkWin(b,c):
    #this avoids deepcopy in a different function
    p = b[c[0]][c[1]]
    return checkHoriz(b,c,p) or checkVert(b,c,p) or checkDiagPos(b,c,p) or checkDiagNeg(b,c,p)

#this is a lot of repetition to optimize assess_board. the threat check takes a very long time!
def checkVertHyp(b,c):
    y = c[1]
    if y<3:
        return 0
    cnc = 1
    yp = b[c[0]][y-1]
    for i in range(y - 2 , -1, -1):
        if b[c[0]][i] != yp:
            break
        else:
            cnc += 1

    if cnc >= 4:
        return yp
    else:
        return 0
def checkHorizHyp(b,c):
    x = c[0]
    y = c[1]
    lc = 0
    lp = 0
    if (x - 1) >= 0:
        lp = b[x-1][y]
        lc = 1
    for i in range(x - 2 , -1, -1):
        if b[i][y] != lp:
            break
        else:
            lc += 1

    rc = 0
    rp = 0
    if (x + 1) < 7:
        rc = 1
        rp = b[x+1][y]
    for i in range(x+2, 7):
        if b[i][y] != rp:
            break
        else:
            rc += 1
    if lc >= 3:
        return lp
    elif rc >= 3:
        return rp
    elif ((rc + lc) >= 3) and (rp == lp):
        return lp
    else:
        return 0
        

def checkDiagPosHyp(b,c):
    y = c[1]
    x = c[0]
    ih = y-x
    if not (-3 <= ih <= 2):
        return 0
    lc = 0
    lp = 0
    if (x - 1) >= 0 and (y-1) >= 0:
        lp = b[x-1][y-1]
        lc = 1
    for i in range(x - 2, -1, -1):
        if (ih + i) <0:
            break
        if b[i][ih + i] != lp:
            break
        else:
            lc += 1
    rc = 0
    rp = 0
    if (x + 1) < 7 and (y+1) < 6:
        rc = 1
        rp = b[x+1][y+1]
    for i in range(x+2,7):
        if (ih+i) > 5:
            break
        if b[i][ih + i] != rp:
            break
        else:
            rp += 1
    if lc >= 3:
        return lp
    elif rc >= 3:
        return rp
    elif ((rc + lc) >= 3) and (rp == lp):
        return lp
    else:
        return 0

def checkDiagNegHyp(b,c):
    y = c[1]
    x = c[0]
    ih = y+x
    if not(3 <= ih <= 8):
        return 0
    
    lc = 0
    lp = 0
    if (x - 1) >= 0 and (y+1) < 6:
        lp = b[x-1][y+1]
        lc = 1
    for i in range(x - 2, -1, -1):
        if (ih - i) >5:
            break
        if b[i][ih - i] != lp:
            break
        else:
            lc += 1
    rc = 0
    rp = 0
    if (x + 1) < 7 and (y-1) >=0:
        rc = 1
        rp = b[x+1][y-1]
    for i in range(x+2,7):
        if (ih - i) <0:
            break
        if b[i][ih - i] != rp:
            break
        else:
            rc += 1

    if lc >= 3:
        return lp
    elif rc >= 3:
        return rp
    elif ((rc + lc) >= 3) and (rp == lp):
        return lp
    else:
        return 0
def checkHypotheticalWin(b,c,):
    return [checkHorizHyp(b,c), checkDiagPosHyp(b,c) , checkDiagNegHyp(b,c)]
    
def assess_board(board,player):
    enemy = 1 if player == 2 else 2
    rating = 0
    sqm = 0
    sqe = 0
    
    total_moves = sqm + sqe
    fc = []
    for x in board:
        fi = 0
        for y in x:
            if y == enemy:
                sqe += 1
            elif y == player:
                sqm += 1
            else:
                fi += 1
        fc.append(fi)
    free = sum(fc)
    #correct parity threat check
    #lower is better except the lowest piece in the column
    
    npt = 0

    for x,col in enumerate(board):
        cpThreatPos = 0
        cpThreatNeg = 0
        for y,pc in enumerate(col):

            if pc != 0 and y>=1:
                hnb = [ board[x+t][y] for t in [-1,1] if (0<= (x+t) <7) ]
                vb = 1 if board[x][y-1] == pc else 0
                hnbs = len([x for x in hnb if x == pc ])
            
                vt = (vb * hnbs) * (-1 if pc == enemy else player)
                rating += vt/2
            if pc == 0 and y>= 1 and col[y - 1] == 0 and cpThreatPos == 0 and cpThreatNeg == 0:
                th = checkHypotheticalWin(board,[x,y])
                is_pos_threat = player in th
                is_neg_threat = enemy in th
                if not (is_pos_threat or is_neg_threat):
                    continue
                other_free_squares = sum(fc[:x] + fc[x+1:]) + y - col.index(0)

                pls = start if sqm == sqe else (start % 2 + 1)
                wwp = ( (pls-1) + other_free_squares ) % 2 + 1

                if is_pos_threat:
                    parity = wwp == player
                    if parity:
                        cpThreatPos = y
                    npt += 0.5
                elif is_neg_threat:
                    parity = wwp == enemy
                    if parity:
                        cpThreatNeg = y
                    npt -= 0.5
        
        rating += sgn(cpThreatPos - cpThreatNeg) * 3
    rating += npt
    if abs(rating) < 2:
        #a knight on the fringe deserves a singe ~Jackson
        fringe_pieces = sum([-1 if t == player else 1 for t in board[0] if t]) + sum([-1 if t == player else 1 for t in board[6] if t])
        rating += sgn(fringe_pieces) * 0.01

    return rating
#to_key seems slow but turns out to save large amounts of time
#with threading there might be a race condition here?
state_lookup = {}

def search(state,depth,m ,op, p, q):
    en = 1 if op == 2 else 2
    global state_lookup
    
    top_ixs_pp = [ [i, (state[i].index(0) - 1) if state[i][5] == 0 else 5] for i in range(7)]
    top_ixs = [x for x in top_ixs_pp if x[1] >= 0]
    wins = [checkWin(state,t) for t in top_ixs]
    
    # large numbers
    if op in wins:
        return 69420
    elif en in wins:
        return -69420 - depth
    if depth == 0:
        return assess_board(state,op) 
    state_key = to_key(state)
    if(state_key in state_lookup):
        return state_lookup[state_key]
    moves = [[i,state[i].index(0)] for i in range(7) if 0 in state[i]]
    if m:
        v = -69420
        for x in moves:
            state[x[0]][x[1]] = op
            v = max(v, search(state,depth-1,False,op, p, q))
            p = max(p, v)
            state[x[0]][x[1]] = 0
            if p >= q:
                break
        state_lookup[state_key] = v
        
        return v
    else:
        v = 69420
        for x in moves:
            state[x[0]][x[1]] = en
            v = min(v,search(state,depth - 1, True, op, p, q))
            q = min(v,q)
            state[x[0]][x[1]] = 0
            if q <= p:
                break
        state_lookup[state_key] = v
        
        return v


def sterge(board,player):
    global start
    enemy = 1 if player == 2 else 2
    lm = 0
    total_moves = sum([ ((lm := x+1) and 1) if board[x][y] != 0 else 0  for y in range(6) for x in range(7) ])
    lm -=1
    #Plays the Skopje opening if starting and responds with the Bishkek defence if playing second
    if total_moves == 0:
        start = player
        return 3
    elif total_moves == 1:
        start = enemy
        return [1,2,3,3,3,4,5][lm]
    global state_lookup
    state_lookup = {}
    #moves = [[i,board[i].index(0)] for i in range(7) if 0 in board[i]] 
    #the one liner looks nicer but this produces better results in the early game
    st = 0
    if len([x for x in board[3] if x]) == total_moves and board[3][4] == 0:
        return 3
    elif board[3][4] != 0 and total_moves <=7:
        st = 1
    assessed_moves = []
    ths = []
    depth = 5
    if total_moves >= 17 :
        depth = 6
    def analyse_move(move,board,player,a,d):
        nb = deepcopy(board)
        nb[move[0]][move[1]] = player
        s = (move[0],search(nb,d, False, player, -69420, 69420 ), )
        a.append(s)
        return
    for x in range(st,7):
        i = 3 + ((x+1)//2) * (-1)**(x)
        if not(0 in board[i]):
            continue
        move = [i,board[i].index(0)]
        th = Thread(target = analyse_move,args = (move, board, player, assessed_moves, depth - 1))
        th.start()
        ths.append(th)
    for x in ths:
        x.join()
    move = max(assessed_moves, key = lambda x: x[1])[0] 
    return move