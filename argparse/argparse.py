#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
argparse.py
"""



# Find here argparse.py, wich is a short script to handle and manage CLI
# args when a program is launched. 

# This script is was written without importing argparse - seems to be too easy 
# for this question


# import

import sys, logging, os	


# logging

l = logging.INFO
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')



def argparse(args=None) : 
	"""
	main function, please https://codingdojo.org/kata/Args/ for more info

	positional args     : - 
	optional args       : -
	return              : List or Dict with typed ans casted args
	raises              : TypeError if -l is not an int
	                      NotADirectoryError if -d is not a directory
	"""

