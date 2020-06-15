# -*- coding: utf-8 -*-
"""
Created on Wed May 28 ‏‎21:18:54 2020

@author: Toshiba

"""
import tkinter
from rand_vs_ai_agent import play,intialize_game
from Game import game_board
from Game import game_state
from alpha_beta_algorithm import alpha_beta
from tkinter import messagebox 

class states_list:
    def __init__(self,arr):
        self.states = arr
        self.index = 0
    def set_list(self,data):
        self.states = data
        self.index = 0
    def get_state(self):
        return self.states[self.index]
    def get_data(self):
        return self.states[self.index].board.board
    def inc_index(self):
        self.index+=1
    def end_game(self):
        if(self.index >= len(self.states)):
            return True
        else:
            return False
        

class player_win:
    name = "name"
    
player = player_win()
player.name = "none"
        
class board_cell:
    
    def __init__(self):
        self.cell = tkinter.Button()
        self.value = 0
    
    def setup_with_color(self , Window , num ,r , c,color):
        self.value = num
        self.cell = tkinter.Button(Window , width = 10 , height = 5 , text = num , bg = color).grid(row=r,column=c)
    
    def setup(self , Window , num ,r , c):
        self.cell = tkinter.Button(Window , width = 10 , height = 5 , text = num , bg="#c7c7c7").grid(row=r,column=c)
    

class game_form:
    def setup(self,arr,tile_pos,score):
        self.board = arr 
        self.tile = tile_pos
        self.window = tkinter.Tk()
        self.window.title("Game Board")
        
        self.cells = [[board_cell(),board_cell(),board_cell()],
                      [board_cell(),board_cell(),board_cell()],
                      [board_cell(),board_cell(),board_cell()]]
        
        tile_row = tile_pos//3
        tile_col = tile_pos%3
        
        for i in range (0,3):
            for j in range(0,3):
                if tile_row == i and tile_col == j:
                    self.cells[i][j].setup_with_color(self.window ,arr[i][j],i,j,'green')
                else:
                    self.cells[i][j].setup(self.window ,arr[i][j],i,j)
        
        tkinter.Label(self.window, text='Score : ' , height = 5).grid(row=3 , column = 0)
        tkinter.Button(self.window ,width = 10 ,text = score , state = "disable").grid(row=3, column = 1)
        
        self.window.geometry('%dx%d+%d+%d' % (240, 330, 50, 200))
    
    def draw( self):
        self.window.mainloop()
    
    def end(self):
        self.window.destroy()


arr = [[1 , -1, 0 ],[1 , 0 , 1 ],[0 , 1 ,-1]]     

control_window =  tkinter.Tk()
control_window.title("Control The game")
control_window.geometry("400x220")
tkinter.Label(control_window, text='Number of movments : ' , height = 5).grid(row=0) 
tkinter.Label(control_window, text='Level Goal : ' , height = 5).grid(row=1) 
e1 = tkinter.Entry(control_window) 
e2 = tkinter.Entry(control_window) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
f = game_form()

all_states = states_list(arr) 

def submit_button():
    m = e1.get()
    s = e2.get()
    max_depth = int(m)
    max_score = int(s)
    all_states.set_list(play(max_depth,max_score,player))


def start_button():
    all_states.index = 0
    f.setup(all_states.get_data(),all_states.get_state().get_tile_position(),all_states.get_state().get_current_score())
    all_states.inc_index()
    
def next_button():
    if all_states.end_game():
        messagebox.showinfo("End of the Game", player.name +" Win")
    else:
        f.end()    
        f.setup(all_states.get_data(),all_states.get_state().get_tile_position(),all_states.get_state().get_current_score())
        all_states.get_state().print_game_state()
        all_states.inc_index()
        f.draw()    

tkinter.Button(control_window ,width = 10 ,text = "Start" , command = start_button).grid(row=2, column = 1)
tkinter.Button(control_window ,width = 10 , text = "Next" , command = next_button).grid(row=2 , column = 2)
tkinter.Button(control_window ,width = 10 , text = "Submit" , command = submit_button).grid(row=2 , column = 0)
    

control_window.mainloop() 



