#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
arg_manager.py
"""


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

