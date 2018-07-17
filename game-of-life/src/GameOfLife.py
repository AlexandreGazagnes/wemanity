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

	# game representation
	__WHITE_SPACE 	= 	' '
	__CELL			= 	'o'

	# exit status 
	__EXIT_STATUS = { 		0 : "game is running / press <Enter> for new round",
							1 : "all cells are dead, game frozen", 
							2 : "max round reached, game ended",
							3 : "game frozen, not evolution can appen (periodicty=1)",
							4 : "game frozen, not evolution can appen (periodicty=2)"}

	def __init__(self, options_dict=None) : 
		""" init method 	
		
		positional args  	: -  
		optional args 		: options dict from arg_manager(), manualy written dict, or None
		do 					: init an GameOfLife object and print out into / welcome msg	
		return 				: a GameOfLife instance
		raise				: - 
		"""

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

			self._cells 		= random.sample(self.__list_of_coords, self._init_cells)
			self._init_cells 	= self._cells

		# else transform user cells in game's cells
		elif isinstance(self._init_cells, list) : 

			self._cells 		= self._init_cells

		# record each cells of last round and last of last round
		# to be able to recon 2 same states of the game 
		self.__last_cells 		= self._cells
		self.__2last_cells 		= self._cells

		# init game_state 
		self._game_state 		= (self._round, self._cells, 0) 


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

	@property	
	def game_state(self):
		return self._game_state
	

	@property	
	def space(self):
		"""this is the UI game representation 
		
		positional args  	: -
		optional args 		: -
		do 					: -
		return 				: return a specific str repr of game space
		raise				: - 
		"""

		txt = "\n"*2

		# game representation / space
		# use pandas.to string, but without index and columns name
		s 	= self._space.to_string(index=False, header=False)
		# replace 0 and 1 with readable values
		s 	= s.replace("0", self.__WHITE_SPACE).replace("1", self.__CELL)
		# add a frame around the sapce to see it 
		s 	= s.replace("\n", "|\n|")
		s 	+="|\n" 
		s 	= "\n|"+s
		s 	= "---" * self.dim + s + "---" * self.dim +"\n"

		# quit if needed
		txt += 	s
		txt += "\n"

		# add game variables 
		txt +=	"round       =  {}\n".format(self.round)
		txt +=	"cells       =  {}\n".format(self.cells_nb)
		txt += 	"\n" *2

		# add game constants
		txt += 	"dim         =  {}\n".format(self.dim)
		txt += 	"max_round   =  {}\n".format(self.max_round)
		txt += 	"init_cells  =  {}\n".format(self.init_cells_nb)
		txt +=	"\n"*2

		txt +=	"press <Crlt + Z> to quit"
		txt +=	"\n"*2
		
		return txt


	def __str__(self) : 
		"""jus overwrite teh __str__ method """
		
		return self.space


	# def __repr__(self) : 
	# 	return self.space


	def neighbours_nb(self, i, j):
		"""for the cell at coord (i,j) give the num of living neighbours (min 0, max 8)"""

		return self.__count_neighbours(i,j)


	def neighbours_loc(self, i,j) : 
		"""for the cell at coord (i,j) give the coords (k,l) of living neighbours"""

		return self.__give_neighbours_coords(i,j)


	def __build_default_space(self) : 
		"""private method : build a space of self.dim ** 2 cells, will all defualt values ie 0/dead
		
		positional args  	: - 
		optional args 		: -
		do 					: -	
		return 				: type pd.DataFrame : empty dataframe (full of 0) of shape self.dim * self.dim
		raise				: - 
		"""

		i = np.arange(self.dim)

		return(pd.DataFrame(0, index=i , columns=i))


	def __update_space(self) : 
		"""method update incorporate cells from self._cells (list of coord of 
		liviving cells in game space represenation

		positional args  	: - 
		optional args 		: -
		do 					: update self._space with self._cells loc as 1 	
		return 				: - 
		raise				: - 
		"""

		# reset an empty space	in a tmp var	
		new_space = self.__build_default_space()

		# replace 0 with 1 if cell in self._cells list 
		for i,j in self._cells : 
			new_space.loc[i,j] = 1 

		# update _space
		self._space = new_space


	def __count_neighbours(self, i,j) : 
		"""count how many living cells for one coord 

		positional args  	: int i, int j wich stands for y, and x coord of a cell
		optional args 		: -
		do 					: -	
		return 				: type int :  number of living neighbours
		raise				: - 
		"""

		# logging.info("__count_neighbours called")

		neighbours = list()
		
		for (i,j) in self.__give_neighbours_coords(i,j) : 
			if self._space.iloc[i,j] == 1 : 
				neighbours.append(1)
		
		return len(neighbours)


	def __give_neighbours_coords(self, i,j)  : 
		"""give all coords of direct neihbourhood for one cells

		positional args  	: int i, int j wich stands for y, and x coord of a cell
		optional args 		: -
		do 					: -	
		return 				: type list : list of tuples (y,x) as coords of existing neighbours
		raise				: - 
		"""

		# logging.info("__give_neighbours_coords called")

		candidates = [	(i+1, j+1), (i-1, j-1),
						(i+1, j-1), (i-1, j+1),
						(i, j-1), (i, j+1),
						(i+1, j), (i-1, j)	]

		autorized = [(i,j) for (i,j) in candidates if (i,j) in self.__list_of_coords]

		return autorized


	def __update_cells(self) : 	
		"""fmethod update to decide, regarding the neighbourhood, if a cell change its statse (living/dead) or 
		stay alive/dead
		rules : if alive with 2/3 neighbours alive : keep living, else is killed 
		        if dead with 3 neighbours : wake up and live else keep deading

		positional args  	: - 
		optional args 		: -
		do 					: update self._cells with live/die rules of the game 	
		return 				: - 
		raise				: - 
		"""

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

		# from living cells : delete cells who die 
		# use list comprehension
		for (i,j) in self._cells : 
			if (i,j) in del_cells : 
				new_cells.remove((i,j))

		# from list of nex living cells extend the curent list 
		new_cells.extend(add_cells)

		self._cells = new_cells


	def __detect_no_lives(self) : 
		"""if cells == 0 stop the game

		positional args  	: -
		optional args 		: -
		do 					: -
		return 				: True if no cells alive, else False 
		raise				: - 
		"""

		if not self._cells  : 
			end_no_lives()
			return True
		return False


	def __detect_last_round(self) : 
		"""if max_round stop the game

		positional args  	: -
		optional args 		: -
		do 					: -
		return 				: True if game's iteration reached  self._max_round, 
							  else False 
		raise				: - 
		"""

		if self._round == self._max_round : 
			end_last_round()
			return True
		return False


	def __detect_game_fixed(self, arg) : 
		""" eval if game fixed with last_round
		
		positional args  	: the cells list to compare to self._cells 
		optional args 		: -
		do 					: -
		return 				: True if game's is fixed, 
							  else False 
		raise				: - 
		"""

		if len(arg) == len(self._cells) : 
			for i in  arg : 
				if i not in self._cells : 
					return False
			end_game_fixed()
			return True
		else : 
			return False


	def __update_game_state(self) : 
		"""regarding sef._cells, self.max_round, etc etc define if games stop or not 
		
		positional args  	: -
		optional args 		: -
		do 					: update self._game_state with self._round, self.cells_nb,
							  and status (ie __EXIT_STATUS)
		return 				: - 
		raise				: -
		"""

		if self.__detect_no_lives() : 
			self._game_state =  (self.round, self.cells_nb, 1)
		
		elif self.__detect_last_round() : 
			self._game_state =  (self.round, self.cells_nb, 2)
		
		elif self.__detect_game_fixed(self.__last_cells) : 
			self._game_state =  (self.round, self.cells_nb, 3)
		
		elif self.__detect_game_fixed(self.__2last_cells) : 
			self._game_state =  (self.round, self.cells_nb, 4)
		
		else : 
			self._game_state =  (self.round, self.cells_nb, 0)


	def __looper(self) : 
		"""find here the looper method wich is used to deal with auto_mode True/Flase
		record last_cells and 2_last_cells to track fixed structures
		and increment round
		
		positional args  	: -
		optional args 		: -
		do 					: handle user interface for next iteration, 
							  update self._round, self.__last_cells and 
							  self.__2last_cells,  
		return 				: - 
		raise				: - 
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


	def _start(self) : 
		"""first game representation for user, ask 

		positional args  	: -
		optional args 		: -
		do 					: update self._space and print it, ask user input to start 
		return 				: - 
		raise				: - 

		"""

		os.system("clear")
		game()

		# game repr
		self.__update_space()
		print(self.space)
		
		# user input 
		print("press <Enter> to start")
		input("press <Crlt + Z> to quit\n")	


	def _next(self) :
		""" update game's state and show game repr for each round

		positional args  	: -
		optional args 		: -
		do 					: update self._cells, self._space, self._game_state 
					    	  and print self._space 
		return 				: - 
		raise				: - 
		"""

		# header + game title
		os.system("clear")
		game()

		self.__update_cells()
		self.__update_space()
		print(self.space)

		self.__update_game_state()
		# if exit status == 0 call __looper() 
		if not self._game_state[2] : 				
			self.__looper()



	def run(self) : 
		"""main method of the game, control strat, loop and exit values of a game
		
		positional args  	: -
		optional args 		: -
		do 					: call self._start()
							   loop on  self._next() 
							  	detect if game exit conditions and break 
							  	or call sefL.__looper before new iteration 
		return 				: 3 dim tuple with self._round, self.cells_nb and exit status   
		raise				: - 
		"""

		# initial state before starting game
		self._start()

		# main loop 
		while True : 

			# call next to upate game's parmas  
			self._next()

			# control game state
			if self._game_state[2] : 
				# if scenario occuring return 3 dim tupple
				return self._game_state






