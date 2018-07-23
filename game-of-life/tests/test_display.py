#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
test_display.py
"""


"""
please use 'pytest -v'
"""   


# import 

import os, sys, logging, pytest


# logging

l = logging.INFO
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')


# change sys.path and import specific module
path = os.path.split(os.getcwd())[0]+"/"
logging.info(path)
sys.path.append(path)
logging.info(sys.path)

from src.display import * 



# functions

def test_intro(monkeypatch) : 
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    intro()


def test_close(monkeypatch) : 
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    close()


def test_header() :
    """ """

    header()


def test_options() :
    """ """

    options()


def test_game(): 
    """ """

    game()


def test_welcome() : 
    """ """

    welcome()


def test_end() : 
    """ """

    end()


def test_end_no_lives(monkeypatch) : 
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    end_no_lives() 


def test_end_last_round(monkeypatch):
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    end_last_round()


def test_end_game_fixed(monkeypatch): 
    """ """

    monkeypatch.setattr('builtins.input', lambda x: "")
    end_game_fixed()


