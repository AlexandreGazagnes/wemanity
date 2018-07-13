#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
test_GameOfLife.py
"""


"""
test collection for GameOfLife.py
please use 'pytest -v'
"""


# import 

import os, sys, logging, pytest

# change sys.path
path = os.path.split(os.getcwd())[0]+"/"
sys.path.append(path)

from src import * 


# logging

l = logging.INFO
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')


# functions

def test_init_GOL() : 
	game = GameOfLife()


def test_next_GOL() : 
	game = GameOfLife()
	game._next()


def test_run_GOL() : 
	game = GameOfLife()
	iteration, exit_value = game.run()
	assert isinstance(iteration, int)
	assert isinstance(exit_value, int)


def test_GOL_block() :
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run() 


def test_GOL_Beehive() : 
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run()


def test_GOL_Loaf() : 
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run()


def test_GOL_Boat() : 
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run()


def test_GOL_Tub() : 
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run()


def test_GOL_Blinker() : 
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run()


def test_GOL_Toad() : 
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run()


def test_GOL_Beacon() : 
	game = GameOfLife(init_cells:[(0,0), (0,0), ...])
	assert (iteration, exit_value) == game.run()


