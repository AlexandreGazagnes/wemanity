#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
test_game-of-life.py
"""


"""
please use 'pytest -v'
"""


# import 

import os, sys, logging, pytest
from src import * 


# logging	

l = logging.INFO
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')


# functions

def test_intro() : 
	"""test intro"""

	assert intro() == 0


def test_close() : 
	"""test close """

	assert close() == 0 


def test_arg_manager0() : 
	"""test arg manager without any cli"""

	options = arg_manager()


# def test_arg_manager1() : 
# 	"""test arg manager with one or 2 max cli"""

# 	# with one or 2 max cli

# 	assert 1 == 0


# def test_arg_manager1() : 
# 	"""test arg manager with all cli avialable """

# 	# with all cli avialable 

# 	assert 1 == 0


def test_GameOfLife0() : 
	"""just init a GameOfLife instance"""

	# just init a GameOfLife with default features

	options 	= arg_manager()
	game 		= GameOfLife(options) 
	
	game.round
	game.dim
	game.cells_loc
	game.init_cells_loc
	game.cells_nb
	game.init_cells_nb
	game.space


def test_GameOfLife1() : 
	"""just init a GameOfLife with defined init cells"""

	options 	= arg_manager()
	options		["init_cells"] = [(2,2), (3,2)]
	game 		= GameOfLife(options) 
	
	game.round
	game.dim
	game.cells_loc
	game.init_cells_loc
	game.cells_nb
	game.init_cells_nb
	game.space
	
	assert (2,2) in game.cells_loc
	assert (3,2) in game.cells_loc
	assert game.neighbours(0,0) == 0

	assert game.neighbours(2,1) == 2
	assert game.neighbours(2,2) == 1

	assert game.neighbours(1,2) == 1
	assert game.neighbours(1,1) == 1

	assert game.neighbours(3,1) == 2
	assert game.neighbours(3,3) == 2
	assert game.neighbours(3,2) == 1

	assert game.neighbours(4,1) == 1
	assert game.neighbours(4,2) == 1
	assert game.neighbours(4,3) == 1

	assert game.neighbours(5,1) == 0
	assert game.neighbours(5,2) == 0
	assert game.neighbours(5,3) == 0






# def test_GameOfLife2() : 
# 	"""just init a GameOfLife instance"""

# 	# just init a GameOfLife with random features
	
# 	assert 1 == 0


# def test_expected_game0() : 
# 	"""run a game session and assert result is conform to game expectation"""

# 	# with just one cell
	
# 	assert 1 == 0


# def test_expected_game1() : 
# 	"""run a game session and assert result is conform to game expectation"""

# 	# with 2  cells

# 	assert 1 == 0
	


# def test_expected_game2() : 
# 	"""run a game session and assert result is conform to game expectation"""

# 	# with 3 cells
	
# 	assert 1 == 0


# def test_expected_game3() : 
# 	"""run a game session and assert result is conform to game expectation"""

# 	# with random state
	
# 	assert 1 == 0


if __name__ == '__main__':
	main()