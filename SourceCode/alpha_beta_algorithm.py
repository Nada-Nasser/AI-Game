# -*- coding: utf-8 -*-
"""
Created on Sun May 24 03:51:20 2020

@author: Toshiba
"""

from Game import game_state
from Board import game_board
import copy

INF = 2147483648
NEG_INF = -2147483648

class alpha_beta:
    
    def minimax(self,current_state ,current_depth , 
                isMaximizingPlayer , alpha , beta ):
        
        if(current_state.isleaf(current_depth)):
            return current_state
        
        if isMaximizingPlayer:
            best_value = copy.deepcopy(create_inf_state(current_state , NEG_INF))
            children = copy.deepcopy(current_state.get_max_children())
                            
            for child in children:
                next_state = copy.deepcopy(self.minimax(child, current_depth+1, False , alpha , beta))
                
                best_value = copy.deepcopy(self.max_state(best_value , next_state))
                
                alpha = copy.deepcopy(self.max_state(alpha , best_value))
                
                if beta.less_than_or_equal(alpha):
                    break
            return best_value
        
        else:
            best_value = copy.deepcopy(create_inf_state(current_state , INF))
            children = copy.deepcopy(current_state.get_min_children())
            
            for child in children:
                next_state = copy.deepcopy(self.minimax(child, current_depth,True , alpha , beta))
                
                best_value = copy.deepcopy(self.min_state(best_value,next_state))
                
                beta = copy.deepcopy(self.min_state(beta,best_value))
                if beta.less_than_or_equal(alpha):
                    break
            return best_value
    
    def max_state(self,state1 , state2):
        score1 = state1.get_current_score()
        score2 = state2.get_current_score()
        if score1 > score2:
            return state1
        else:
            return state2
    
    def min_state(self,state1 , state2):
        score1 = state1.get_current_score()
        score2 = state2.get_current_score()
        if score1 < score2:
            return state1
        else:
            return state2
        
    
 

def create_inf_state(current_state , inf):
    inf_arr = [[inf,inf,inf] , [inf,inf,inf] , [inf,inf,inf]]
    inf_board = game_board(inf_arr,current_state.get_tile_position())
    inf_state = game_state(inf_board,current_state.max_depth,current_state.max_score,inf)  
    return inf_state

def key(obj):
    return obj.key()

def sort_max_children(children):
    children.sort(key = key , reverse=True)

def sort_min_children(children):
    children.sort(key = key)
    