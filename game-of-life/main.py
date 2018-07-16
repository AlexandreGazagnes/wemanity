#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
kata_gol.py
"""


"""
find here the main function for my representtaion of the game-of-life
"""


# import 

import os, sys, logging
from src import * 


# logging	

l = logging.WARNING
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')


# main


def main() : 


	gol = GameOfLife(options)
	gol.run()

	close()




if __name__ == '__main__':
	main()