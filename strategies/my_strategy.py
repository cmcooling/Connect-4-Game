## I guess the way with the highest winning rate is to use DQN/Q-learning by dnn but it will waste too much time. Xp

def my_strategy(board, player_number):
    ''' # Chris edit - indented docstring
    Basicly what I am doing here is to check whether there is risk of losing one step ahead, and if there is, minimize it. 
    other part is similar with random strategy(or I can do the similar risk check for my opponent and try to maximize 
    the risk for the opponent)
    '''
    import numpy as np
    board = np.array(board)
    if player_number == 1 :
        enemy_position = np.where(board==1)
        max_row = np.max(enemy_position[:,0]) 
        enemy_position = enemy_position.T
        for i in range(max_row):
            
            if enemy_position[:,0].count(i-1) == 2:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1

                if not board[i-1][col+2]:
                    return col+2

            if enemy_position[:,0].count(i-1) == 3:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1
                if not board[i-1][col+3]:
                    return  col+3
            
        for i in range(np.max(enemy_position[:,1])): # Chris edit - added close parenthesis
            if enemy_position[:,1].count(i-1) == 3:
                return i-1

       
        row_num = enemy_position.shape[0]
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
        
        return(random.randint(0, 6))



    
    if player_number == 2 :
        enemy_position = np.where(board==1)
        max_row = np.max(enemy_position[:,0]) 
        enemy_position = enemy_position.T
        for i in range(max_row):
            
            if enemy_position[:,0].count(i-1) == 2:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1

                if not board[i-1][col+2]:
                    return col+2

            if enemy_position[:,0].count(i-1) == 3:
                col = enemy_position.index(i-1)
                if not board[i-1][col-1]:
                    return col-1
                if not board[i-1][col+3]:
                    return  col+3
            
        for i in range(np.max(enemy_position[:,1])): # Chris edit - added close parenthesis
            if enemy_position[:,1].count(i-1) == 3:
                return i-1

       
        row_num = enemy_position.shape[0]
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
        
        return(random.randint(0, 6))