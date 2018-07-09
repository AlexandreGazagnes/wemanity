#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
__init__.py
"""


# import 
import os, sys, argparse, logging


# constants 

SIZE 		= None 		# space dim
INIT_STATE	= None		# number of random cells

MAX_ROUND 	= None		# ask to jump /stop an x number of loop

AUTO 		= False		# auto or handly new loop
WAITER 		= 1 		# second



# functions

def intro() : 
	"""basic welcome screen with print out instcuctions to stdout

	positional args  	: - 
	optional args 		: -
	do 					: print out welcome message 	
	return 				: 0 
	raises				: - 
	"""

	print("hello")

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

	d = dict(	auto=AUTO, size=SIZE, init_cells = init_cells, 
				waiter=WAITER, max_round=max_round)
	
	return d


def close() : 

	"""basic bye screen with print out ending message to stdout

	positional args  	: - 
	optional args 		: -
	do 					: print out ending message 	
	return 				: 0 
	raises				: - 
	"""

	print("close")

	return 0



# class 

class GameOfLife(object) : 

	def __init__(self.options_dict) : 
		"""init method"""


		self._space 	= None
		self._cells 	= None
		self._round 	= 0


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


