#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:35:33 2022

@author: shimin
"""

import os
import sys
sys.path.extend([os.path.dirname(os.path.abspath(""))])
#print(sys.path)
from copy import deepcopy
import random
from victory_check import check_victory


def sam(board, player_number):
    #print(board)
    def lossfunction(board, player_number):
        v = check_victory(board)
        if v == player_number:
            return -1
        elif v == 0:
            return 0
        else:
            return 1
        
    decision_list = [0] * 7
    for i, j in enumerate(board):
        try:
            board2 = deepcopy(board)
            board2[i][j.index(0)] = player_number
            decision_list[i] = lossfunction(board2, player_number)
            
            if decision_list[i] != -1:
                temp_list = []
                for k,l in enumerate(board2):
                    try:
                        board3 = deepcopy(board2)
                        board3[k][l.index(0)] = 3-player_number
                        temp_list += [lossfunction(board3, player_number)]
                    except ValueError:
                        pass
                decision_list[i] = max(temp_list)

        except ValueError:
            decision_list[i] = 2
    print(decision_list)
    if decision_list == [2]*7:
        try:
            for i,j in enumerate(board):
                if j[-1] == 0:
                    return i
        except:
            pass
    return random.choice([i for i, x in enumerate(decision_list) if x == min(decision_list)])

            