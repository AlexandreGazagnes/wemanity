#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
arg_manager.py
"""


"""
find here all arguments manager instructions
eg arg_manager is the main function, wich will call an argument builder and all arguments user interface ("ask") and checking ("check") functions
this arg_manager could become a class in the next tags, just to increase code readability
see various docstrings bellow for more information
"""


# import 

import os, sys, argparse, logging
from src.consts import *
from src.display import options


# functions

def default_args() : 
	"""return default argumennts

	positional args  	: - 
	optional args 		: -	
	return 				: dict object with key/values of arguments 
	raises				: - 
	"""

	logging.info("default_args() called")

	options = dict(		dim 		= DIM_DEFAULT, 
						init_cells 	= INIT_CELLS_DEFAULT, 
						auto_mode 	= AUTO_MODE, 
						waiter 		= WAITER_DEFAULT,
						max_round 	= MAX_ROUND_DEFAULT)

	check_options(options) 

	return options




def check_dim(dim) : 
	""" """

	param = True
	if not isinstance(dim, int) : 
		param = False
		print("TypeError(dim type error, expected <class 'int'>, recieved {}".format(type(dim)))
	
	if dim > DIM_MAX :
		param = False
		print("ValueError(dim value error, expected max {}, recieved {}".format(DIM_MAX, dim))

	if dim < DIM_MIN :
		param= False
		print("ValueError(dim value error, expected min {}, recieved {}".format(DIM_MIN, dim))
	if not param : 
		print("we will ask you to choose this parametre manualy :(")
		return False
	return True
