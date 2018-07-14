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


##############################################
##############################################
##############################################


def ask_dim() : 
	""" """
	msg =	"\n\n" + \
			"please choose the dimension of games's space : \n\n" + \
			"\texpected an {} with min {} and max {} \n".format(type(DIM_MAX), DIM_MIN, DIM_MAX) + \
			"\teg dim = 3 will build a 3 * 3 space with 9 cases \n" + \
			"\tpress <Enter> for default value : {}\n".format(DIM_DEFAULT) + \
			"\tpress <Ctrl+Z> to quit \n" + \
			"\n"
	
	os.system("clear")

	options()

	while True : 

		dim = input(msg)

		if not dim : 
			return DIM_DEFAULT

		try : 
			dim = int(dim)
			if dim > DIM_MAX : 
				print("\n\ndim value error, expected max {}, recieved {}".format(DIM_MAX, dim))
			elif dim < DIM_MIN : 
				print("\n\ndim value error, expected min {}, recieved {}".format(DIM_MIN, dim))
			else : 
				return dim 
		except : 
			print("\n\ndim type error, expected {}, recieved {}".format(type(DIM_MAX),type(dim)))



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

	decor_param(param)

	return param


def check_auto_mode(auto_mode) : 
	""" """
	
	param = True 
	if not isinstance(auto_mode, bool) : 
		param = False
		print("TypeError(auto_mode type error, expected <class 'bool'>, recieved {}".format(type(auto_mode)))

	decor_param(param)

	return param


def check_init_cells(init_cells) : 
	""" """
 	pass


def check_waiter(waiter) : 
	""" """
	
	param=True
	if not ((isinstance(waiter, int)) or (isinstance(waiter, float)) ): 
		print("TypeError(waiter type error, expected <class 'int' / 'float'>, recieved {}".format(type(waiter)))
	if waiter > WAITER_MAX :
		param=False		
		print("ValueError(waiter value error, expected max {}, recieved {}".format(WAITER_MAX, waiter))
	if waiter < WAITER_MIN :
		param = False
		print("ValueError(waiter value error, expected min {}, recieved {}".format(WAITER_MIN, waiter))

	decor_param(param)

	return param


def check_max_round(max_round) : 
	""" """

	param = True
	if not isinstance(max_round, int) : 
		param = False
		print("TypeError(max_round type error, expected <class 'int'>, recieved {}".format(type(max_round)))
	if max_round > MAX_ROUND_MAX :
		param = False
		print("raise ValueError(max_round value error, expected max {}, recieved {}".format(MAX_ROUND_MAX, max_round))
	if max_round < MAX_ROUND_MIN :
		param = False
		print("ValueError(max_round value error, expected min {}, recieved {}".format(MAX_ROUND_MIN, max_round))

	decor_param(param)

	return param


def decor_param(param) : 
	""" """

	if not param : 
		print("we will ask you to choose this parametre manualy :(")

