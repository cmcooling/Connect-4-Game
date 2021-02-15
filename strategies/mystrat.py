def beginner_strat(board, player_number):
    for i_column in range(0,7):
        if player_number == 1:
            for ind0 in range (3,5):
                if board[3][0] != 0 and board[4][0] != 0: break
                elif board[3][0] == 0:
                    return 3
                elif board[3][0] != 0:
                    return 4
            for ind1 in range (3,5):
                if board[4][5] != 0 or board[3][5] != 0 or board[3][2] == 2 or board[4][2] == 2 or board[3][3] == 2 or board[4][3] == 2: break
                elif board[3][1] == 0:
                    return 3
                elif board[3][1] != 0 and board[3][1] == 2:
                    return 4
                elif board[3][0] == 1 and board[3][1] == 1and board[3][2] == 1:
                    return 3
                elif board[3][1] != 0 and board[3][1] == 1 and board[3][3] == 2:
                    return 4
                elif board[3][1] != 0 and board[3][1] == 1 and board[3][3] != 2:
                    return 3
                elif board[3][1] != 0 and board[3][1] == 1 and board[3][3] == 0:
                    return 3
            for ind2 in range (0,7):
                if board[4][2] == 2 or board[4][3] == 2: break 
                elif board[4][1] == 0 or 1:
                    return 4
            for ind3 in range (0,7):
                if board[4][3] == 2 or board[3][3] == 2 or board[3][4] == 2 or board[3][5] == 2: break
                elif board[4][2] == 2 and board[3][2] == 0:
                    return 3
            for ind4 in range (0,7):
                if board[6][1] == 2: break
                elif board[4][2] == 1 and board[6][0] == 0:
                    return 6
            for ind5 in range (0,7):
                if board [5][2] == 2: break
                elif board[4][2] == 1 and board[6][0] == 1 and board[5][0] != 0:
                    return 5
            for ind6 in range (0,7):
                if board [2][3] == 0:
                    return 2
                elif board [2][3] != 0: break
            for ind_final_1 in range(0,7):
                if board[1][5] != 0: break
                return 1
            for ind_final_0 in range(0,7):
                if board[0][5] != 0: break
                return 0
            for ind_final_2 in range(0,7):
                if board[2][5] != 0: break
                return 2
            for ind_final_5 in range(0,7):
                if board[5][5] != 0: break
                return 5
            for ind_final_6 in range(0,7):
                if board[6][5] != 0: break
                return 6
            
               
        if player_number == 2:
            for ind0 in range (3,5):
                if board[3][0] != 0 and board[4][0] != 0: break
                if board[3][0] == 0:
                    return 3
                elif board[3][0] != 0:
                    return 4
            for ind1 in range (3,5):
                if board[4][5] != 0 or board[3][5] != 0 or board[3][2] == 1 or board[4][2] == 1 or board[3][3] == 1 or board[4][3] == 1: break
                elif board[3][1] == 0:
                    return 3
                elif board[3][1] != 0 and board[3][1] == 1:
                    return 4
                elif board[3][0] == 1 and board[3][1] == 1and board[3][2] == 1:
                    return 3
                elif board[3][1] != 0 and board[3][1] == 2 and board[3][3] == 1:
                    return 4
                elif board[3][1] != 0 and board[3][1] == 2 and board[3][3] != 1:
                    return 3
                elif board[3][1] != 0 and board[3][1] == 2 and board[3][3] == 0:
                    return 3
            for ind2 in range (0,7):
                if board[4][2] == 1 or board[4][3] == 1: break 
                elif board[4][1] == 0 or 2:
                    return 4
            for ind3 in range (0,7):
                if board[4][3] == 1 or board[3][3] == 1 or board[3][4] == 1 or board[3][5] == 1: break
                elif board[4][2] == 1 and board[3][2] == 0:
                    return 3
            for ind4 in range (0,7):
                if board[6][1] == 1: break
                elif board[4][2] == 2 and board[6][0] == 0:
                    return 6
            for ind5 in range (0,7):
                if board [5][2] == 1: break
                elif board[4][2] == 2 and board[6][0] == 2 and board[5][0] != 0:
                    return 5
            for ind6 in range (0,7):
                if board [2][3] == 0:
                    return 2
                if board [2][3] != 0: break
            for ind_final_1 in range(0,7):
                if board[1][5] != 0: break
                return 1  
            for ind_final_0 in range(0,7):
                if board[0][5] != 0: break
                return 0
            for ind_final_2 in range(0,7):
                if board[2][5] != 0: break
                return 2
            for ind_final_5 in range(0,7):
                if board[5][5] != 0: break
                return 5
            for ind_final_6 in range(0,7):
                if board[6][5] != 0: break
                return 6
            
                    
    
                
            
        
        


