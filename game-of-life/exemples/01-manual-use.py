#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
01-manual-use.py
"""


"""
for a manual use, you can import and check manualy every class argument for 
each round

behind the woods, GameOfLife.run() call 2 methods : first one time GameOfLife._start() 
and after call GameOfLife._next() until game'end.

you can manualy call theses methods


------------------------------------------------------------------------------



# From python / ipython / atom / spyder (...) interpreter : 
------------------------------------------------------------------------------

# import manualy : 
from src import *

# init manualy option's dict :
# options = arg_manager()		# UNCOMMENT THIS LINE IF NEEDED 

# or use default_args() -> automatic (no user input) arg manager with defaults 
# args :
options = default_args()


# init game instance :
game = GameOfLife(options)


# print out game parameters : 
print(game.dim)
print(game.auto_mode)
print(game.waiter)
print(game.max_round)
print(game.init_cells_loc)
print(game.init_cells_nb)

# then run it :  
# game.run() 	# UNCOMMENT THIS LINE IF NEEDED 


# or for a more painful usage : 

# first :
game._start()

# and then : 
game._next()
game._next()
game._next()
game._next()
# ...

# you can control attibute's values for each round : 
print(game.round)
print(game.cells_nb)
print(game.cells_loc)
print(game.neighbours_nb(2,2))
print(game.neighbours_loc(2,2))
print(game.state)
  

# when you are tired to call _next() you can call run() : 
# game.run() 	# UNCOMMENT THIS LINE IF NEEDED 


""