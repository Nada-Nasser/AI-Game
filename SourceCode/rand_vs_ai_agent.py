# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:46:40 2020

@author: Toshiba

"""
from Game import game_board
from Game import game_state
from alpha_beta_algorithm import alpha_beta
import copy

def play(depth,score,player):
    
    max_depth = depth
    max_score = score
    random_min = True
    state = intialize_game(max_depth,max_score)
    
    current_depth = 0
    MAX_PLAYER = True
    INF = 2147483648
    NEG_INF = -2147483648
    current_score = 0
    game = alpha_beta()  # constructor do nothig
    
    all_states = []
    all_states.append(copy.deepcopy(state))
    while True:
        current_score = state.get_current_score()
        
        max_player_win = is_max_win(max_depth,max_score,current_depth,current_score)
        max_player_loss = is_max_loss(max_depth,max_score,current_depth,current_score)          
        
        
        if max_player_win:
            player.name = "MAX Player"
            break
        
        if  max_player_loss:
            player.name = "MIN Player"
            break
        
        if MAX_PLAYER:
            alpha = create_inf_state(state,NEG_INF)
            beta = create_inf_state(state,INF)
            
            state.set_parent(None) # root of the alpha beta tree
            best_state = game.minimax(state, 1, True, alpha, beta)
            
            state = best_state.get_original_state_from_leaf()
            
            all_states.append(copy.deepcopy(state))
            
            current_depth += 1
            
            MAX_PLAYER = False
        else:
            if random_min:
                state.move_to_random_min_child()
            else:    
                alpha = create_inf_state(state,NEG_INF)
                beta = create_inf_state(state,INF)
                
                state.set_parent(None) # root of the alpha beta tree
                best_state = game.minimax(state, 1, False, alpha, beta)
                
                state = best_state.get_original_state_from_leaf()
         
            MAX_PLAYER = True
    
    return all_states

###############################################################################

def create_inf_state(current_state , inf):
    inf_arr = [[inf,inf,inf] , [inf,inf,inf] , [inf,inf,inf]]
    inf_board = game_board(inf_arr,current_state.get_tile_position())
    inf_state = game_state(inf_board,current_state.max_depth,current_state.max_score,inf)
   
    return inf_state

def is_max_win(max_depth,max_score,current_depth,current_score):
    if (current_depth <= max_depth and current_score >= max_score):
        return True
    else:
        return False

def is_max_loss(max_depth,max_score,current_depth,current_score):
    if (current_depth >= max_depth and current_score < max_score):
        return True
    else:
        return False

def intialize_game(max_depth,max_score):
    board_values = [[1 , -1, 0 ]
                   ,[1 , 0 , 1 ],
                    [0 , 1 ,-1]]
    board = game_board(board_values,6)
    state = game_state(board,max_depth,max_score,0)    
    return state
