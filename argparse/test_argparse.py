#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
tests 
"""


# import

import pytest, unittest, os
from argparse import argparse


"""
please use "pytest -v" rather than unittest
"""


# functions

def test_do_not_raise_error() :
	"""test program don not fail in normal conditions"""
	
	os.system("python3 argparse.py -l -p 8080 -d /home/")
	os.system("python3 argparse1.py -l -p 8080 -k 12222 -f 'sdnie' -d /home/")


def test_do_raise_error() : 
	""" test good exception are raised"""

	with pytest.raises(TypeError) : 
		argparse("python3 argparse.py -p 80aa80 ")

	with pytest.raises(NotADirectoryError) : 		
		argparse("python3 argparse.py -d -usr-logs")


def test_detect_args() : 
	"""test good return of argparse function"""

	args = argparse("python3 argparse.py -l -p 8080 -d /home/")
	assert len(args) == 3
	assert isinstance(args, dict)	


# main	

if __name__ == '__main__':
	main()