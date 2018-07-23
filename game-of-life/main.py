#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
main.py
"""


"""
find here the main function of the game-of-life
"""


# import 

import os, sys, logging
from src import * 


# logging	

l = logging.WARNING
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')


# main

def main() : 

	game = GameOfLife()
	game.run()


if __name__ == '__main__':
	main()
