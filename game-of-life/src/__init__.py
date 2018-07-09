#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
__init__.py
"""


# import 

import os, sys, argparse, logging, random

import pandas as pd
import numpy as np

from src import * 


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




# functions

def intro() : 
	"""basic welcome screen with print out instcuctions to stdout

	positional args  	: - 
	optional args 		: -
	do 					: print out welcome message 	
	return 				: 0 
	raises				: - 
	"""

	logging.info("intro() called")

	os.system("clear")

	msg = str(	"#########################################\n"
				"\n"
				"              GAME OF LIFE               \n"
				"\n"
				"#########################################\n"
				"\n\n")

	print(msg)

	return 0



def close() : 

	"""basic bye screen with print out ending message to stdout

	positional args  	: - 
	optional args 		: -
	do 					: print out ending message 	
	return 				: 0 
	raises				: - 
	"""

	logging.info("closeo() called")



	msg = str(	"#########################################\n"
				"\n"
				"              bye bye bye !!!             \n"
				"\n"
				"#########################################\n"
				"\n\n")

	print(msg)

	return 0


def arg_manager() : 
	"""basic args manager using argpare

	positional args  	: - 
	optional args 		: -	
	return 				: dict object with key/values of arguments 
	raises				: - 
	"""

	args = sys.args[1:]

	# manage args from cli or display fancy user interface to ask user
	# default return something before writting full funct

	d = dict(	dim=DIM_DEFAULT, init_cells=INIT_CELLS_DEFAULT, 
				auto_mode = AUTO_DEFAULT, 
				waiter=WAITER_DEFAULT, max_round=MAX_ROUND_DEFAULT)
	
	return d






# class 

class GameOfLife(object) : 


	# class consts

	__white_space 	= 	' '
	__cell			= 	'o'


	def __init__(self, options_dict) : 
		"""init method"""

		logging.info("init a new GameOfLife object")

		# init attr
		[ self.__setattr__(str("_"+key), val) for key, val in options_dict.items() ]

		_index = np.arange(self.dim)
		self._space  = pd.DataFrame(0, index=_index , columns=_index)
		self.__default_space = self._space

		self._turn 	= 0


		self._list_of_coord = [	(i,j) 	for i in range(self._dim) 
											for j in range(self._dim)]

	def run(self, round) : 
		"""launch a game session"""

		print("init space")
		print(self._space)

		input("enter to start")

		cont = True
		while cont : 


			# update params
			self.__update_cells()
			self.__update_space()


			# auto/manual next turn 
			if self.auto : 	
				time.sleep(self.waiter)
			else : 			
				input("enter to continue")

			# if cells == 0 stop the game
			if not self.cells  : 
				cont = False


			# if max_round stop the game
			if self.round == self.max_round : 
				cont = False
				print("end")

			self.round+=1


	@property
	def foo(self):
		"""proprety of important attributes"""

		pass
	

	def __str__(self) : 
		"""over write the str method"""
		
		pass
		

	def __update_space(self) : 
		"""update space representation from cells list"""

		pass


	def __update_cells(self) : 
		"""define from rules living/dying cells for each round"""

		pass


