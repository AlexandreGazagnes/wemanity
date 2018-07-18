#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
02-specific-args-use.py
"""


"""



------------------------------------------------------------------------------



# From python / ipython / atom / spyder / jupyter(...) interpreter : 
------------------------------------------------------------------------------

# import manualy : 
from src import *


# OPTION 1
# options = {dim:25, auto_mode:True, waiter:1, max_round:200, init_cells=200}

OPTION 1 bis
# options = {dim:25}

OPTIONS 2

# options = {dim:25, auto_mode:True, waiter:1, max_round:200, init_cells=200}
options = arg_manager(options)

OPTION 2 bis
# options = {dim:25}
options = arg_manager(options)

OPTION 3 
options = arg_manager()


OPTIONS 4
options = None


# init game instance :
game = GameOfLife(options)

# then run it :  
# game.run() 					# UNCOMMENT THIS LINE IF NEEDED 

"""
