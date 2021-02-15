import numpy as np
import random as random
def my_strategy(board, player_number):
    
    board = np.array(board)
    if player_number == 1 :
        enemy_position = np.where(board==2)
        enemy_position = np.array(enemy_position)
        enemy_position = enemy_position.T
       
        for i in range(np.max(enemy_position[:,0])):
            if len(np.argwhere(enemy_position[:,0]==i-1)) == 2:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1

                if not board[i-1][col+2]:
                    return col+2

            if len(np.argwhere(enemy_position[:,0]==1))== 3:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1
                if not board[i-1][col+3]:
                    return  col+3
            
        for i in range(np.max(enemy_position[:,1])):
            if len(np.argwhere(enemy_position[:,1]==i-1)) == 3:
                return i-1

       
        row_num = enemy_position.shape[0]
        try:
            for i in range(row_num):
                piv = enemy_position[i-1]
           
                if board[piv[0]+1][piv[1]+1]==2:
                    if board[piv[0]+2][piv[1]+2]==2:
                        if board[piv[0]+2][piv[1]+3]:
                            return piv[1]+3
                        if board[piv[0]+1][piv[1]+3]:
                            return piv[1]+2
                    else:
                        return random.randint(0,6)
        except IndexError:
                return random.randint(0,6)
        
        return(random.randint(0, 6))



    
    if player_number == 2 :
        enemy_position = np.where(board==1)
        enemy_position = np.array(enemy_position)
        enemy_position = enemy_position.T
       
        for i in range(np.max(enemy_position[:,0])):
            
            
            if len(np.argwhere(enemy_position[:,0]==i-1)) == 2:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1

                if not board[i-1][col+2]:
                    return col+2

            if len(np.argwhere(enemy_position[:,0]==1))== 3:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1
                if not board[i-1][col+3]:
                    return  col+3
            
        for i in range(np.max(enemy_position[:,1])):
            if len(np.argwhere(enemy_position[:,1]==i-1)) == 3:
                return i-1

       
        row_num = enemy_position.shape[0]
        try:
            for i in range(row_num):
                piv = enemy_position[i-1]
           
                if board[piv[0]+1][piv[1]+1]==2:
                    if board[piv[0]+2][piv[1]+2]==2:
                        if board[piv[0]+2][piv[1]+3]:
                            return piv[1]+3
                        if board[piv[0]+1][piv[1]+3]:
                            return piv[1]+2
                    else:
                        return random.randint(0,6)
        except IndexError:
                return random.randint(0,6)
        
        return(random.randint(0, 6))