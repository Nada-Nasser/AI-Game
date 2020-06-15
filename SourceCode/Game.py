# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:35:49 2020

@author: Toshiba
"""
import copy
from Board import game_board
import random

class game_state:
#    board , max_depth , max_score
    def __init__(self, board , max_depth , max_score , curr_score):
        self.parent_state = None
        self.board = copy.deepcopy(board)
        self.max_depth = max_depth
        self.max_score = max_score
        self.current_score = curr_score
    
    def isleaf(self,current_depth):
        if self.current_score >= self.max_score or current_depth >= self.max_depth:
            return True
        else:
            return False
        
    def print_game_state(self):
        self.board.print_game_board()
        print("current_score = " , self.current_score)
        print("-------------------------------------")
     
    def get_current_score(self):
        return self.current_score
    
    def get_tile_position(self):
        return self.board.tile_position
    
    def get_max_children(self):
        parent = copy.deepcopy(self)
        
        children = []
        current_board = copy.deepcopy(self.board)
                
        if current_board.can_move_down():
            self.board.move_down()
            new_score = self.current_score + self.board.get_value_at_tile()
            child_down = create_game_state(self.board ,self.max_depth,self.max_score,new_score)
            child_down.parent_state = copy.deepcopy(parent)
            children.append(child_down)
        self.board = copy.deepcopy(current_board)

        if current_board.can_move_right():
            self.board.move_right()
            new_score = self.current_score + self.board.get_value_at_tile()           
            child_right = create_game_state(self.board ,self.max_depth,self.max_score,new_score)
            child_right.parent_state = copy.deepcopy(parent)
            children.append(child_right)
        self.board = copy.deepcopy(current_board)
        
        if current_board.can_move_left():
            self.board.move_left()
            new_score = self.current_score + self.board.get_value_at_tile()
            child_left = create_game_state(self.board ,self.max_depth,self.max_score,new_score)
            child_left.parent_state = copy.deepcopy(parent)
            children.append(child_left)
        self.board = copy.deepcopy(current_board)

        if current_board.can_move_up():
            self.board.move_up()
            new_score = self.current_score + self.board.get_value_at_tile()
            child_up = create_game_state(self.board,self.max_depth,self.max_score,new_score)
            child_up.parent_state = copy.deepcopy(parent) 
            children.append(child_up)       
        self.board = copy.deepcopy(current_board)

        return children
        
        
    def get_min_children(self):
         
        parent = copy.deepcopy(self)        
        children = []
        current_board = copy.deepcopy(self.board)
        
        self.board.set_at_prev_tile(1)
        child1 = create_game_state(self.board,self.max_depth,self.max_score,self.current_score)
        child1.parent_state = copy.deepcopy(parent)
        children.append(child1)
        self.board = copy.deepcopy(current_board)
        
        self.board.set_at_prev_tile(0)
        child2 = create_game_state(self.board,self.max_depth,self.max_score,self.current_score)
        child2.parent_state = copy.deepcopy(parent)
        children.append(child2)
        self.board = copy.deepcopy(current_board)
        
        self.board.set_at_prev_tile(-1)
        child3 = create_game_state(self.board,self.max_depth,self.max_score,self.current_score)
        child3.parent_state = copy.deepcopy(parent)
        children.append(child3)
        self.board = copy.deepcopy(current_board)
        
        return children

    def move_to_random_min_child(self):
        value = random.randint(-1,1)
        parent = copy.deepcopy(self)        
        self.board.set_at_prev_tile(value)
        self.parent_state = copy.deepcopy(parent)
       
    def less_than_or_equal(self,state2):
        score2 = state2.get_current_score()
        if self.current_score <= score2:
            return True
        else:
            return False
    
    def set_parent(self,parent):
        self.parent_state = parent
    
    def get_original_state_from_leaf(self):
        curr_state = copy.deepcopy(self)
        
        while curr_state.parent_state.parent_state != None:
            curr_state = copy.deepcopy(curr_state.parent_state)
            
        return curr_state
    
    def key(self):
        return self.current_score
    
def create_game_state(board,max_depth,max_score,current_score):
    state = game_state(copy.deepcopy(board),max_depth,max_score,current_score)
    return state

        
     
        