# -*- coding: utf-8 -*-
"""
Created on Sun May 24 03:17:56 2020

@author: Toshiba
"""

class game_board:
    # board , tile_position , prev_tile_position
    prev_board = []
    def __init__(self, arr,tile):
        self.prev_tile_position = 6
        self.board = arr
        self.tile_position = tile
        self.row_index = self.tile_position//3
        self.col_index = self.tile_position%3
         
    def print_game_board(self):
        for row in self.board:
            print(row)
        print("tile position = " , self.tile_position)
    
    # if tile position != 0,1,2
    def can_move_up(self):
        if (self.tile_position != 0 
            and self.tile_position!=1 
            and self.tile_position!=2):
            return True
        else:
            return False
        
    # if tile position != 6,7,8
    def can_move_down(self):
        if (self.tile_position != 6 
            and self.tile_position!=7 
            and self.tile_position!=8):
            return True
        else:
            return False
    
    # if tile position != 2,5,8
    def can_move_right(self):
        if (self.tile_position % 3 != 2 
            and self.tile_position % 3 != 5
            and self.tile_position % 3 != 8): 
            return True
        else:
            return False
    
    # if tile position != 0,3,6    
    def can_move_left(self):
        if (self.tile_position != 0 
            and self.tile_position != 3 
            and self.tile_position != 6): 
            return True
        else:
            return False
    
    #tile_position -= 3 
    def move_up(self):
        self.prev_tile_position = self.tile_position
        self.row_index = self.tile_position//3
        self.col_index = self.tile_position%3
        self.tile_position -= 3
        self.board[self.row_index-1][self.col_index] += self.board[self.row_index][self.col_index]  
        self.board[self.row_index][self.col_index] = '?'
    
    def move_down(self):
        self.prev_tile_position = self.tile_position
        self.row_index = self.tile_position//3
        self.col_index = self.tile_position%3
        self.tile_position += 3
        self.board[self.row_index+1][self.col_index] += self.board[self.row_index][self.col_index]  
        self.board[self.row_index][self.col_index] = '?'
    
    def move_right(self):
        self.prev_tile_position = self.tile_position
        self.row_index = self.tile_position//3
        self.col_index = self.tile_position%3
        self.tile_position += 1
        self.board[self.row_index][self.col_index+1] += self.board[self.row_index][self.col_index]  
        self.board[self.row_index][self.col_index] = '?'
    
    def move_left(self):
        self.prev_tile_position = self.tile_position
        self.row_index = self.tile_position//3
        self.col_index = self.tile_position%3
        self.tile_position -= 1
        self.board[self.row_index][self.col_index-1] += self.board[self.row_index][self.col_index]  
        self.board[self.row_index][self.col_index] = '?'
    
    def set_at_prev_tile(self,num):
        row = self.prev_tile_position//3
        col = self.prev_tile_position%3
        self.board[row][col] = num
    
    def get_value_at_tile(self):
        self.row_index = self.tile_position//3
        self.col_index = self.tile_position%3
        curr_score = self.board[self.row_index][self.col_index]
        return curr_score
