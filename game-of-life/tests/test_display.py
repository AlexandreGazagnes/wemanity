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

# change sys.path
path = os.path.split(os.getcwd())[0]+"/"
sys.path.append(path)

from src import * 


# logging

l = logging.INFO
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')


