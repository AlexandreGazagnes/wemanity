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

from src.GameOfLife import * 
from src.arg_manager import *

# logging

l = logging.INFO
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')


# functions

def test_init_GOL(monkeypatch) : 
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    options = default_args()
    game = GameOfLife(options)


def test_next_GOL(monkeypatch) : 
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    options = default_args()
    game = GameOfLife(options)
    game._next()


def test_run_GOL(monkeypatch) :
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    options = dict(dim=5, auto_mode=True, waiter=0.0, max_round=100)
    game = GameOfLife(options)

    iteration, nb_cells, exit_value = game.run()
    assert isinstance(iteration, int)
    assert isinstance(exit_value, int)
    assert isinstance(nb_cells, int)


def test_GOL_block(monkeypatch) :
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    init_cells = [(1,1), (1,2), (2,1), (2,2)]
    options = dict( dim=5, 
                    auto_mode=True, 
                    waiter=0.0, 
                    max_round=100, 
                    init_cells=init_cells)
    game = GameOfLife(options)

    assert (0, 4, 3) == game.run() 



def test_GOL_Beehive(monkeypatch) : 
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    init_cells = [(2,2), (2,3), (3,3), (3,1), (4,2)]
    options = dict( dim=5, 
                    auto_mode=True, 
                    waiter=0.0, 
                    max_round=100, 
                    init_cells=init_cells)
    game = GameOfLife(options)
    assert (0, 5, 3) == game.run() 


# def test_GOL_Loaf() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_Boat() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_Tub() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_Blinker() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_Toad() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_Beacon() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_config0() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_config1() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_config2() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


# def test_GOL_config3() : 
#   """ """

#   monkeypatch.setattr('builtins.input', lambda x: "")
#   init_cells = [(1,1), (1,2), (2,1), (2,2)]
#   options = dict( dim=5, 
#                   auto_mode=True, 
#                   waiter=0.0, 
#                   max_round=100, 
#                   init_cells=init_cells)
#   game = GameOfLife(options)

#   assert (0, 4, 3) == game.run() 


