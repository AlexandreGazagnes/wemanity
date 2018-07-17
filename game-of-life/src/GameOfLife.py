#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
GameOfLife.py
"""


"""
find here the main class of our project GameOfLife. Our argument manager (arg_manager) is called directly from the __init__ methode for good readability of game-of-life/main.py.
a specific effort regarding private args and method was done :)
see all information bellow in doctrings and comments 
enjoy :) :)
"""


# import 

import os, sys, argparse, logging, random, time

import pandas as pd
import numpy as np

from src.display import *
from src.arg_manager import * 


# class 

class GameOfLife(object) : 


	# class consts

	__white_space 	= 	' '
	__cell			= 	'o'


	def __init__(self, options_dict=None) : 
		""" """

		# print intro
		intro()

		
		# if options -> check and ask, else arg_manager from scratch
		options_dict = arg_manager(options_dict)

		# init attr from options
		[ self.__setattr__(str("_"+key), val) for key, val in options_dict.items() ]

		# build default space fill with 0
		i = np.arange(self.dim)
		self._space  			= self.__build_default_space()
		self.__default_space 	= self.__build_default_space()

		# round
		self._round = 0

		# list of all valid coord of the space
		self.__list_of_coords = [	(i,j) 	for i in range(self._dim) 
											for j in range(self._dim)]

		# if user just give a number => init a random location of cells 
		if isinstance(self._init_cells, int) : 

			self._cells = random.sample(self.__list_of_coords, self._init_cells)
			self._init_cells = self._cells

		# else transform user cells in game's cells
		elif isinstance(self._init_cells, list) : 

			self._cells = self._init_cells

		# record each cells of last round and last of last round
		# to be able to recon 2 same states of the game 
		self.__last_cells = self._cells
		self.__2last_cells = self._cells

		# incorporate list of cells to the game represntation
		self._update_space()


	@property
	def round(self):
		return self._round


	@property
	def max_round(self):
		return self._max_round


	@property
	def init_cells_loc(self):
		return self._init_cells


	@property
	def init_cells_nb(self):
		return len(self._init_cells)


	@property
	def dim(self):
		return self._dim


	@property	
	def cells_loc(self):
		return self._cells


	@property	
	def cells_nb(self):
		return len(self._cells)

	# @property
	# def last_cells(self):
	# 	return self.__last_cells

	# @property
	# def last_2cells(self):
	# 	return self.__2last_cells
	

	@property	
	def space(self):
		"""this is the UI game representation """

		txt = "\n"*4

		# game representation / space
		# use pandas.to string, but without index and columns name
		s 	= self._space.to_string(index=False, header=False)
		# replace 0 and 1 with readable values
		s 	= s.replace("0", self.__white_space).replace("1", self.__cell)
		# add a frame around the sapce to see it 
		s 	= s.replace("\n", "|\n|")
		s 	+="|\n" 
		s 	= "\n|"+s
		s 	= "---" * self.dim + s + "---" * self.dim +"\n"

		# quit if needed
		txt += 	s
		txt +=	"\n"*2
		print("press <Crlt + Z> to quit")
		txt +=	"\n"*2

		# add game variables 
		txt +=	"round       =  {}\n".format(self.round)
		txt +=	"cells       =  {}\n".format(self.cells_nb)
		txt += 	"\n" *2

		# add game constants
		txt += 	"dim         =  {}\n".format(self.dim)
		txt += 	"max_round   =  {}\n".format(self.max_round)
		txt += 	"init_cells  =  {}\n".format(self.init_cells_nb)
		
		return txt


	def __str__(self) : 
		return self.space


	# def __repr__(self) : 
	# 	return self.space


	def neighbours_nb(self, i, j):
		"""for the cell at coord (i,j) give the num of living neighbours (min 0, max 8)"""

		return self.__count_neighbours(i,j)


	def neighbours_loc(self, i,j) : 
		"""for the cell at coord (i,j) give the coords (k,l) of living neighbours """

		return self.__give_neighbours_coords(i,j)


	def __build_default_space(self) : 
		"""private method : build a space of self.dim ** 2 cells, will all defualt values ie 0/dead"""

		i = np.arange(self.dim)
		return(pd.DataFrame(0, index=i , columns=i))


	def _update_space(self) : 
		"""method update incorporate cells from self._cells (list of coord of liviving cells in game space represenation"""

		# reset an empty space	in a tmp var	
		new_space = self.__build_default_space()

		logging.info(self._cells)

		# replace 0 with 1 if cell in self._cells list 
		for i,j in self._cells : 
			new_space.loc[i,j] = 1 

		update _space
		self._space = new_space


	def _update_cells(self) : 	
		"""fmethod update to decide, regarding the neighbourhood, if a cell change its statse (living/dead) or 
		stay alive/dead
		rules : if alive with 2/3 neighbours alive : keep living, else is killed 
		        if dead with 3 neighbours : wake up and live else keep deading""" 


		# create 2 empty list of cells one to add and one to dell 
		add_cells 	= list()
		del_cells 	= list()
		
		# considering living cells 
		for i,j in self.__list_of_coords :
			# count how many neighbours  
			neighbours = self.__count_neighbours(i,j)

			# if 2 or 3 neighbours --> stay alive 
			if (i,j) in self._cells : 
				if (neighbours == 2) or (neighbours == 3) : 
					pass
				# if less or more --> die 
				else :
					del_cells.append((i,j))

			# considering dead cells  
			else : 
				# if 3 neighbours --> wake up and live
				if neighbours == 3 : 
					add_cells.append((i,j))
				else :
					# else stay dead
					pass

		# copy _cells in a tmp var
		new_cells = list(self._cells)

		logging.info({(i,j) : self.neighbours_nb(i,j) for i,j in self._cells})


		# from living cells : delete cells who die 
		# use list comprehension
		for (i,j) in self._cells : 
			if (i,j) in del_cells : 
				new_cells.remove((i,j))

		# from list of nex living cells extend the curent list 
		new_cells.extend(add_cells)

		self._cells = new_cells


	def __count_neighbours(self, i,j) : 
		"""count how many living cells for one coord """

		# logging.info("__count_neighbours called")

		neighbours = list()
		
		for (i,j) in self.__give_neighbours_coords(i,j) : 
			if self._space.iloc[i,j] == 1 : 
				neighbours.append(1)
		
		return len(neighbours)


	def __give_neighbours_coords(self, i,j)  : 
		"""give all coords of direct neihbourhood for one coord"""

		# logging.info("__give_neighbours_coords called")

		candidates = [	(i+1, j+1), (i-1, j-1),
						(i+1, j-1), (i-1, j+1),
						(i, j-1), (i, j+1),
						(i+1, j), (i-1, j)	]

		autorized = [(i,j) for (i,j) in candidates if (i,j) in self.__list_of_coords]

		return autorized


	def _next(self) :
		""" update game's state and show game repr"""			

		self._update_cells()
		self._update_space()
		print(self.space)


	def __looper(self) : 
		"""find here the looper method wich is used to deal with auto_mode True/Flase
		record last_cells and 2_last_cells to track fixed structures
		and increment round
		"""

		# if auto_mode just sleep a certain time 
		if self._auto_mode : 
			time.sleep(self._waiter)

		# else ask to user input before continuing
		else : 
			input( "press <Enter> for next iteration"
					"press <Crlt + Z> to quit \n")

		# incremenent round
		self._round+=1
		# record last list of cells for dectecting fixed game (periodicity =1)
		self.__last_cells = self._cells
		# record lastof last  list of cells for dectecting fixed game (periodicity =2)		
		if self._round %2 : 
			self.__2last_cells = self._cells


	def __detect_no_lives(self) : 
		"""if cells == 0 stop the game"""

		if not self._cells  : 
			end_no_lives()
			return True


	def __detect_last_round(self) : 
		"""if max_round stop the game"""

		if self._round == self._max_round : 
			end_last_round()
			return True


	def __detect_game_fixed(self, arg) : 
		""" eval if game fixed with last_round"""

		if len(arg) == len(self._cells) : 
			for i in  arg : 
				if i not in self._cells : 
					return False
			end_game_fixed()
			return True
		else : 
			return False
	

	def run(self) : 
		"""main method of the game, control strat, loop and exit values of a game
		"""

		# initial state before starting game
		# header + game title
		os.system("clear")
		game()
		# game repr
		print(self.space)
		# user input 
		print("press <Enter> to start")
		input("press <Crlt + Z> to quit\n")	

		# useless????
		self.__cont = True

		# main loop 
		while self.__cont : 
			# header + game title
			os.system("clear")
			game()

			# call next to upate game status 
			self._next()

			# control game state , and return tupple if one end scenario 
			# is ocuring
			if self.__detect_no_lives() : 
				logging.info(1)
				return self.round, self.cells_nb, 1
			if self.__detect_last_round() : 
				logging.info(2)
				return self.round, self.cells_nb, 2
			if self.__detect_game_fixed(self.__last_cells) : 
				logging.info(3)
				return self.round, self.cells_nb, 3
			if self.__detect_game_fixed(self.__2last_cells) : 
				logging.info(4)
				return self.round, self.cells_nb, 4
			else : 
				# else just do "loop operartions and go on for an other loop"
				self.__looper()


