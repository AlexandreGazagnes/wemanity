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



# Comamnd Line Interface
------------------------------------------------------------------------------

# in your cli, type  : 

-- $ python3 [your-path]/game-of-life.main.py -- 

or 
 
-- $ chmod +x [your-path]/game-of-life.main.py  --
-- $ [your-path]/game-of-life.main.py  -- 



------------------------------------------------------------------------------



# From python / ipython / atom / spyder (...) interpreter : 
------------------------------------------------------------------------------

# import manualy : 
from src import GameOfLife

# init game instance :
game = GameOfLife()

# then run it :  
game.run()


