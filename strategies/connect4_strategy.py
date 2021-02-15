import random

def starting_move(): 
    return (3)

def second_strategy (board, player):
    if player == 1:
        empty = []
        x_filled = []
        o_filled = []
        for rows in range(6):
            for column in range(7): 
                if board[column][rows]==0:
                    empty+=[[column, rows]]
                elif board[column][rows]==1:
                    if rows<6:
                        if board[column][rows+1]== 0:
                            x_filled.insert(0, [column, rows])
                        else:
                            x_filled.insert(-1, [column, rows])
                    else:
                            x_filled.insert(-1, [column, rows])
                elif board[column][rows]==2:
                    o_filled+=[[column, rows]]
                    
        
        if len(x_filled) == 0: 
            return (3)
        else: 
            pass
             
        for i in o_filled:
            if board[i[0]][i[1]+1] == 2:
                return(i[0])


             
        if len(x_filled) > 0 :
            for i in x_filled:
                print(i)
                if board[i[0]][i[1]+1] == 0 and i[1] <= 6:
                    return(i[0])
                elif board[i[0]][i[1]+1] == 1:
                    pass
                elif board[i[0]][i[1]+1] == 2:
                    return(random.randint(0, 6))
    elif player == 2:
        empty = []
        x_filled = []
        o_filled = []
        for rows in range(6):
            for column in range(7): 
                if board[column][rows]==0:
                    empty+=[[column, rows]]
                elif board[column][rows]==2:
                    if rows<6:
                        if board[column][rows+1]== 0:
                            x_filled.insert(0, [column, rows])
                        else:
                            x_filled.insert(-1, [column, rows])
                    else:
                        x_filled.insert(-1, [column, rows])
                elif board[column][rows]==1:
                    o_filled+=[[column, rows]]
                    
        
        if len(x_filled) == 0: 
            return (3)
        else: 
            pass
                          
        if len(x_filled) > 0 :
            for i in x_filled:
                print(i)
                if board[i[0]][i[1]+1] == 0 and i[1] <= 6:
                    return(i[0])
                elif board[i[0]][i[1]+1] == 2:
                    pass
                elif board[i[0]][i[1]+1] == 1:
                    return(random.randint(0, 6))
            
