#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
consts.py
"""


# constants 

# game dimension
DIM_MIN 		= 5
DIM_DEFAULT 	= 10
DIM_MAX 		= 20

# if  INT --> # numb of cells in the space
INIT_CELLS_DEFAULT 	= int(0.1 * DIM_DEFAULT**2)
INIT_CELLS_MIN 		= 1
INIT_CELLS_MAX 		= DIM_MAX

# if LIST of Tuples --> defaul location for cels
# INIT_CELLS = [(3,2), (3,3) ...]

# auto mode eg loop without user input 
AUTO_DEFAULT 	= False
WAITER_DEFAULT 	= 0.5
WAITER_MIN		= 0.1
WAITER_MAX 		= 1

# posible stop to avoid infinite loop
MAX_ROUND_DEFAULT = 10
