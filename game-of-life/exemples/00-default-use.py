#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
00-default-use.py
"""


"""
for default use, you can use the Linux interpreter or any python interpreter.

all features, settings and methods are provided directly by the GameOfLife 
class.

it contains a complete and fancy user interface that will guide you in using 
the game.

let yourself go and everything will be fine



------------------------------------------------------------------------------



# Comand Line Interface
------------------------------------------------------------------------------

in your cli, type  : 
-- $ python3 [your-path]/GameOfLife.main.py -- 
or 
 
-- $ chmod +x [your-path]/GameOfLife.main.py  --
-- $ [your-path]/GameOfLife.main.py  -- 



------------------------------------------------------------------------------



# From python / ipython / atom / spyder etc etc interpreter : 
------------------------------------------------------------------------------
import manualy : 

from [your-path]/GameOfLife.src.GameOfLife import * 
from [your-path]/GameOfLife.src.GameOfLife import GameOfLife
from [your-path]/GameOfLife.src import * 
from [your-path]/GameOfLife.src import GameOfLife


# init game instance :
game = GameOfLife()

# run :  
game.run()

"""

