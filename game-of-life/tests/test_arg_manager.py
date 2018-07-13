#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
test_arg_manager.py
"""


"""
test collection for arg_manager.py
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

def test_init_args() : 
	arg_manager()


def test_valid_args() : 
	arg_manager(dict(dim=10, auto_mode=True, waiter=0.3, max_round=100, init_cells=20, ))


def test_invalid_args_dim() : 
	assert False == check_dim(-1)
	assert False == check_dim(1000)
	assert False == check_dim("aaa")
	assert False == check_dim(list())
	assert False == check_dim(True)

def test_valid_args_dim() : 
	assert True == check_dim(12)
	assert True == check_dim(20)
	assert True == check_dim(25)


def test_invalid_args_auto_mode() : 
	assert False == check_auto_mode(1000)
	assert False == check_auto_mode(-1)
	assert False == check_auto_mode("aaa")
	assert False == check_auto_mode(list())


def test_valid_args_auto_mode() : 
	assert True == check_auto_mode(True)
	assert True == check_auto_mode(False)


def test_invalid_args_waiter() : 
	assert False == check_waiter(-1)
	assert False == check_waiter("aa")
	assert False == check_waiter(10)
	assert False == check_waiter(True)


def test_valid_args_waiter() : 
	assert True == check_waiter(0.1)
	assert True == check_waiter(1)
	assert True == check_waiter(1.2)
	assert True == check_waiter(2.33333)


def test_invalid_args_max_round() : 
	assert False == check_max_round(10000)
	assert False == check_max_round(-1)
	assert False == check_max_round("aaa")
	assert False == check_max_round(list())


def test_valid_args_max_round() : 
	assert True == check_max_round(10)
	assert True == check_max_round(300)
	assert True == check_max_round(500)
	assert True == check_max_round(1000)


def test_invalid_args_init_cells() : 
	pass


def test_no_args() : 
	assert [ask_dim, ask_auto ask_init_cells] == args_detector()
	 

def test_full_args() :
	assert [] == args_detector(dict(dim=10,auto_mode=True, waiter=0.3, max_round=100, init_cells=20, ))


def test_partial_args0() : 
	pass


def test_partial_args1() : 
	pass


def test_partial_args2() : 
	pass


def test_partial_args3() : 
	pass


def cli_args() :
	pass


