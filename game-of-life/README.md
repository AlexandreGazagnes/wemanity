# Game of Life


## Short
-------------------------------------------------------
Find here my work about game-of-life which is a project more complex whatever that of an intermediary level, it is of my vision of the game of life of conway which is one of the most known cellular automata : https://bitstorm.org/gameoflife/. Initially it was not asked to code the whole game of life but one thing bringing another the project is so far almost complete.


## Description
-------------------------------------------------------
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced players, by creating patterns with particular properties. 

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
* Any live cell with fewer than two live neighbors dies, as if by under population.
* Any live cell with two or three live neighbors lives on to the next generation. 
* Any live cell with more than three live neighbors dies, as if by overpopulation. 
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations. source wikipedia


## Version
-------------------------------------------------------
1.2.0

## Licence
-------------------------------------------------------
GNU GENERAL PUBLIC LICENSE


## Requirements
-------------------------------------------------------
* python  v3.5+
* pytest  
* pandas  v0.20.3+
* numpy   v1.12.0+
	

## Download
-------------------------------------------------------
```cd
git clone https://github.com/AlexandreGazagnes/wemanity/tree/master/game-of-life
cd game-of-life/
```

## Install
-------------------------------------------------------
    
no install
    
    

## Usage
-------------------------------------------------------

### CLI
standard : ```python3 game-of-life/main.py```

advanced : ```python3 game-of-life/main.py + [-d /--dim VAL] [-r/--max_round VAL] [-a/--auto_mode VAL] [-w /--waiter VAL] [-c/--cells VAL]```

where : 
*  -d / --dim is :      the dimension
*  -a/--auto_mode is :  auto iterate or ask <Enter> from user input for each iteration
*  -w /--waiter is :    refresh time laps (auto mode only)
*  -r / --max_round :   number max of iterations (auto mode only)
*  -c/--cells is :      the number or positions of initial living cells



### Python Interpreter (python, ipython, atom, spyder, jupyter...) : 

```
from src import GameOflife (or import *)
g = GameOfLife()
g.run()
```
for more exemples please see exemples/


## Folder  
-------------------------------------------------------
* exemples/      : various scripts about use cases 
* main.py        : main scrpit 
* README.md      : readme
* src/	         : sources files, functions class etc etc
* tests/         : test scripts 

