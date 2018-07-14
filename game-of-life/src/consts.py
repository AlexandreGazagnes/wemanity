#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
consts.py
"""


"""
find here all important features with 3 main values : Default, Min and Max
These consts are temporarly in a separate file but should be moved in an ArgManager class as Class constants
see various comments bellow for more information
"""


# constants 

# game dimension
DIM_DEFAULT 		= 20
DIM_MIN 			= 5
DIM_MAX 			= 30

# if  INT --> # numb of cells in the space
INIT_CELLS_DEFAULT 	= int(0.4 * DIM_DEFAULT**2)
INIT_CELLS_MIN 		= 1
INIT_CELLS_MAX 		= int(DIM_MAX*0.75)

# if LIST of Tuples --> defaul location for cels
# INIT_CELLS = [(3,2), (3,3) ...]

# auto mode eg loop without user input 
AUTO_MODE_DEFAULT	= True

WAITER_DEFAULT 		= 0.2
WAITER_MIN			= 0.1
WAITER_MAX 			= 3

# posible stop to avoid infinite loop
MAX_ROUND_DEFAULT 	= 300
MAX_ROUND_MIN 		= 10
MAX_ROUND_MAX 		= 1000
