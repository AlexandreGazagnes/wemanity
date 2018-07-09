#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
tests 
"""


# import

import pytest, unittest, os
from my_argparse import my_parser


"""
please use "pytest -v" rather than unittest
"""


# functions

def test_do_not_raise_error() :
	"""test program don not fail in normal conditions"""

	os.system("python3 my_argparse.py")
	os.system("python3 my_argparse.py -l ")
	os.system("python3 my_argparse.py -p 8080 ")
	os.system("python3 my_argparse.py -d /home/")
	os.system("python3 my_argparse.py -l -p 8080 -d /home/")
	os.system("python3 my_argparse.py -l -p 8080 -k 12222 -f 'sdnie' -d /home/")

def test_do_raise_error() : 
	""" test good exception are raised"""

	with pytest.raises(TypeError) : 
		my_parser(1226789)

	with pytest.raises(TypeError) : 
		my_parser("python3 my_argparse.py -p 80aa80 ")

	with pytest.raises(NotADirectoryError) : 		
		my_parser("python3 my_argparse.py -d -usr-logs")


def test_detect_args0() : 
	"""test good return of argparse function"""

	args = my_parser("python3 my_argparse.py -l -p 8080 -d /home/")
	assert len(args) == 3
	assert isinstance(args, dict)	


def test_detect_args1() : 
	"""test good return of argparse function"""

	args = my_parser("python3 my_argparse.py")
	assert len(args) == 3
	assert isinstance(args, dict)	


def test_detect_args2() : 
	"""test good return of argparse function"""

	args = my_parser("python3 my_argparse.py -l -p 8080 -d /home/ -k False -v 122 ")
	assert len(args) == 3
	assert isinstance(args, dict)	


# main	

if __name__ == '__main__':
	main()
