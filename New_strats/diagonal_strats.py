#%%
import random
from New_strats import open_lane_check, height_count

def check_pos_diag(board,player_number):
    
    keylanes=[]
    dangerlanes=[]
    playernos=[1,2]
    playernos.remove(player_number)
    opponent_number = playernos[0]
    
    #to check for 3 in a row
    for i_column_start in range(0,4):
        for i_row_start in range(0,3):
            
            start_owner = board[i_column_start][i_row_start]
            
            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start+3][i_row_start+3]==opponent_number:
                continue

            for i in range(3):
                if board[i_column_start + i][i_row_start + i] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start+3)
                if (i_row_start-height+4)==1:
                    keylanes.append(i_column_start+3)
                elif (i_row_start-height+4)==2:
                    dangerlanes.append(i_column_start+3)
                    
    for i_column_start in range(1,5):
        for i_row_start in range(1,4):
            start_owner = board[i_column_start][i_row_start]

            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start-1][i_row_start-1]==opponent_number:
                continue

            for i in range(3):
                if board[i_column_start + i][i_row_start + i] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start-1)
                if (i_row_start-height)==1:
                    keylanes.append(i_column_start-1)
                elif (i_row_start-height)==2:
                    dangerlanes.append(i_column_start-1)
                    
    #to check for 2+1
    for i_column_start in range(4):
        for i_row_start in range(0,3):
            start_owner = board[i_column_start][i_row_start]
            
            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start+2][i_row_start+2]==opponent_number:
                continue
            
            column_ranges=[i_column_start,i_column_start+1,i_column_start+3]
            row_ranges=[i_row_start,i_row_start+1,i_row_start+3]

            for i in range(3):
                if board[column_ranges[i]][row_ranges[i]] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start+2)
                if (i_row_start-height+3)==1:
                    keylanes.append(i_column_start+2)
                elif (i_row_start-height+3)==2:
                    dangerlanes.append(i_column_start+2)
    
    for i_column_start in range(2,6):
        for i_row_start in range(2,5):
            start_owner = board[i_column_start][i_row_start]

            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start-1][i_row_start-1]==opponent_number:
                continue
            
            column_ranges=[i_column_start,i_column_start+1,i_column_start-2]
            row_ranges=[i_row_start,i_row_start+1,i_row_start-2]

            for i in range(3):
                if board[column_ranges[i]][row_ranges[i]] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start-1)
                if (i_row_start-height)==1:
                    keylanes.append(i_column_start-1)
                elif (i_row_start-height)==2:
                    dangerlanes.append(i_column_start-1)
                    
    return [keylanes,dangerlanes]

def check_neg_diag(board,player_number):
    
    keylanes=[]
    dangerlanes=[]
    playernos=[1,2]
    playernos.remove(player_number)
    opponent_number = playernos[0]

    #to check for 3 in a row
    for i_column_start in range(0,4):
        for i_row_start in range(3,6):
            start_owner = board[i_column_start][i_row_start]
            
            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start+3][i_row_start-3]==opponent_number:
                continue

            for i in range(3):
                if board[i_column_start + i][i_row_start - i] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start+3)
                if (i_row_start-height-2)==1:
                    keylanes.append(i_column_start+3)
                elif (i_row_start-height-2)==2:
                    dangerlanes.append(i_column_start+3)
                    
    for i_column_start in range(1,5):
        for i_row_start in range(2,5):
            start_owner = board[i_column_start][i_row_start]

            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start-1][i_row_start+1]==opponent_number:
                continue

            for i in range(3):
                if board[i_column_start + i][i_row_start - i] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start-1)
                if (i_row_start-height+2)==1:
                    keylanes.append(i_column_start-1)
                elif (i_row_start-height+2)==2:
                    dangerlanes.append(i_column_start-1)
                    
    #to check for 2+1
    for i_column_start in range(4):
        for i_row_start in range(3,6):
            start_owner = board[i_column_start][i_row_start]

            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start+2][i_row_start-2]==opponent_number:
                continue
            
            column_ranges=[i_column_start,i_column_start+1,i_column_start+3]
            row_ranges=[i_row_start,i_row_start-1,i_row_start-3]

            for i in range(3):
                if board[column_ranges[i]][row_ranges[i]] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start+2)
                if (i_row_start-height-1)==1:
                    keylanes.append(i_column_start+2)
                elif (i_row_start-height-1)==2:
                    dangerlanes.append(i_column_start+2)
    
    for i_column_start in range(2,6):
        for i_row_start in range(1,4):
            start_owner = board[i_column_start][i_row_start]

            if start_owner==0:
                continue

            elif start_owner!=player_number:
                continue
            
            elif board[i_column_start-1][i_row_start+1]==opponent_number:
                continue
            
            column_ranges=[i_column_start,i_column_start+1,i_column_start-2]
            row_ranges=[i_row_start,i_row_start-1,i_row_start+2]

            for i in range(3):
                if board[column_ranges[i]][row_ranges[i]] != start_owner:
                    break
            else:
                height=height_count.count(board,i_column_start-1)
                if (i_row_start-height+2)==1:
                    keylanes.append(i_column_start-1)
                elif (i_row_start-height+2)==2:
                    dangerlanes.append(i_column_start-1)
                    
    return [keylanes,dangerlanes]

def check_diag(board,player_number):
    keylanes1=check_pos_diag(board,player_number)[0]
    keylanes2=check_neg_diag(board,player_number)[0]
    dangerlanes1=check_pos_diag(board,player_number)[1]
    dangerlanes2=check_neg_diag(board,player_number)[1]
    keylanes=keylanes1+keylanes2
    dangerlanes=dangerlanes1+dangerlanes2
    return [keylanes,dangerlanes]

def blocking_diagonal(board,player_number):
    lanes=open_lane_check.check(board)
    playernos=[1,2]
    playernos.remove(player_number)
    opponent_number=playernos[0]
    
    block = check_diag(board,opponent_number)[0]
    block = [x for x in block if x in lanes]
    
    danger = check_diag(board,opponent_number)[1]
    
    if len(block)!=0:
        return random.choice(block)        
    else:
        return danger

def winning_diagonal(board,player_number):
    lanes=open_lane_check.check(board)
    
    win = check_diag(board,player_number)[0]
    win = [x for x in win if x in lanes]
    
    bait = check_diag(board,player_number)[1]
    
    if len(win)!=0:
        return random.choice(win)          
    else:
        return bait
    
def diagonal_strat(board,player_number):
    lanes=open_lane_check.check(board)
    win=winning_diagonal(board,player_number)
    block=blocking_diagonal(board,player_number)
    if type(win)==int :
        print('using win h')
        return win
    elif type(block)==int:
        print('using block h')
        return block
    else:
        danger=block
        bait=win     
        
        no_trouble=[x for x in lanes if x not in danger+bait]
        print(no_trouble)
        no_more_baits=[x for x in lanes if x not in danger]
        forced_lost=danger
        
        if len(no_trouble)!=0:
            return random.choice(no_trouble)
        
        elif len(no_more_baits)!=0:
            return random.choice(no_more_baits)
        
        else:
            return random.choice(forced_lost)

    
#%%
board=[[2,2,2,1,0,0],[2,0,0,0,0,0],[2,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[2,2,1,0,0,0],[2,2,2,1,0,0]]
check_diag(board,2)
blocking_diagonal(board,2)
#winning_diagonal(board,1)
diagonal_strat(board,2)