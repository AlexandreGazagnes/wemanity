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

def arg_manager() : 
	"""basic args manager using argpare
	positional args  	: - 
	optional args 		: -	
	return 				: dict object with key/values of arguments 
	raises				: - 
	"""

	logging.info("arg_manager() called")

	args = sys.argv[1:]

	# manage args from cli or display fancy user interface to ask user
	# default return something before writting full funct

	d = dict(	dim=16, init_cells=40, 
				auto_mode = True, 
				waiter=1,
				max_round=40)
	
	return d

