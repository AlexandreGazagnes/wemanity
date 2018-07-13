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


	def __init__(self, options_dict) : 
		"""init method"""

		logging.info("init a new GameOfLife object")

		# init attr
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

		# else 
		elif isinstance(self._init_cells, list) : 

			self._cells = self._init_cells

		else :
			raise ValueError("invalid init state")

		logging.info(self._cells)

		self._update_space()

		logging.info("end of init")



	@property
	def round(self):
		return self._round


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
	def space(self):

		txt = "\n"*4

		s 	= self._space.to_string(index=False, header=False)
		s 	= s.replace("0", self.__white_space).replace("1", self.__cell)
		s 	= s.replace("\n", "|\n|")
		s 	+="|\n" 
		s 	= "\n|"+s
		s 	= "---" * self.dim + s + "---" * self.dim +"\n"

		txt += s
		txt +="\n"
		txt +="round  = {}\n".format(self.round)
		txt +="cells  = {}\n".format(self.cells_nb)
		txt += "\n" * 4

		return txt


	def __str__(self) : 
		return self.space


	def __repr__(self) : 
		return self.space


	def neighbours_nb(self, i, j):
		return self.__count_neighbours(i,j)


	def neighbours_loc(self, i,j) : 
		return self.__give_neighbours_coords(i,j)


	def __build_default_space(self) : 

		i = np.arange(self.dim)
		return(pd.DataFrame(0, index=i , columns=i))


	def _update_space(self) : 
		"""update space regarding cells coords"""

		logging.info("update_space called")

		s = "\n" + str(self._space) ; s = s.replace("0", " ")
		logging.info("old _space") 
		logging.info(s)
		
		new_space = self.__build_default_space()

		logging.info(self._cells)
		for i,j in self._cells : 
			new_space.loc[i,j] = 1 

		self._space = new_space

		s = "\n" + str(self._space) ; s = s.replace("0", " ")
		logging.info("new _space")
		logging.info(s)


	def _update_cells(self) : 	
		"""for each round update wich cell live or die"""

		logging.info("update_cells called")

		add_cells 	= list()
		del_cells 	= list()
		
		for i,j in self.__list_of_coords : 
			neighbours = self.__count_neighbours(i,j)

			if (i,j) in self._cells : 
				if (neighbours == 2) or (neighbours == 3) : 
					pass
				else :
					del_cells.append((i,j))

			else : 
				if neighbours == 3 : 
					add_cells.append((i,j))
				else :
					pass

		new_cells = list(self._cells)
		logging.info("new_cells  = copy _cells list")
		logging.info(new_cells)
		logging.info(self._cells)

		logging.info({(i,j) : self.neighbours_nb(i,j) for i,j in self._cells})

		logging.info("add_cells list")
		logging.info(add_cells)

		logging.info("del_cells list")
		logging.info(del_cells)

		for (i,j) in self._cells : 
			if (i,j) in del_cells : 
				new_cells.remove((i,j))

		logging.info("_cells after remove")
		logging.info(new_cells)

		new_cells.extend(add_cells)

		logging.info("_cells after extend")
		logging.info(new_cells)
		self._cells = new_cells
		logging.info(self._cells)


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

		self._update_cells()
		self._update_space()


	def run(self) : 
		"""launch a game session"""

		print("init space")
		os.system("clear")
		print(self.space)

		input("enter to start")

		cont = True
		while cont : 
			os.system("clear")

			self._next()
			print(self.space)

			# if cells == 0 stop the game
			if not self._cells  : 
				cont = False
				print("no more cells living")

			# if max_round stop the game
			if self._round == self._max_round : 
				cont = False
				print("last round")

			self.__looper()
			
		print("end")


	def __looper(self) : 

		if self._auto_mode : 
			time.sleep(self._waiter)
			print("press <Crlt + C> to quit")
		else : 
			input("press <Enter> for next turn or <Crlt + C> to quit \n")

		self._round+=1


