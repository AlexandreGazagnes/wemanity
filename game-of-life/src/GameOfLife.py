#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
GameOfLife.py
"""


"""
find here the main class of our project GameOfLife. Our argument manager 
(arg_manager) is called directly from the __init__ method for better readability
of game-of-life/main.py.

a specific effort regarding private args and method was done :)

to improve readability, lots of code refactoring options was not applied.

see all information bellow in doctrings or ins comments 
"""


# import 

import os, logging, random, time

import pandas as pd
import numpy as np

from src.display import *
from src.arg_manager import * 


# class 

class GameOfLife(object) : 


    # class consts

    # game representation
    __DEAD_CELL   =   ' '
    __LIVING_CELL =   'o'

    # exit status 
    __EXIT_STATUS = {   0 : "game is running / press <Enter> for new round",
                        1 : "all cells are dead, game ended", 
                        2 : "max round reached, game ended",
                        3 : "game frozen, no more evolution possible (periodicty=1)",
                        4 : "game frozen, no more evolution possible (periodicty=2)"}


    def __init__(self, options_dict=None) : 
        """init method  
        
        positional args     : -  
        optional args       : option's dict (from arg_manager or manualy written)
                              or None
                              if option's dict is not 'None', arg_manager will
                              automaticly check all data and ask user inputs
                              if wrong data type or value  
        do                  : init an GameOfLife object and print out 
                              into / welcome msg    
        return              : a GameOfLife object
        raise               : - 
        """

        # print intro
        intro()

        # if options -> check and ask, else ask arg_manager to manage user 
        # interface and to build a valid options_dict from scratch
        options_dict                = arg_manager(options_dict)

        # init attr from options with an '_' before to control user acces to 
        # specific attributes
        [ self.__setattr__(str("_"+key), val) 
                                        for key, val in options_dict.items() ]

        # build default space fill with 0
        i = np.arange(self.dim)
        self._space                 = self.__build_default_space()
        self.__default_space        = self.__build_default_space()

        # round counter for each iteration
        self._round = 0

        # list of all valid coords of the space
        self.__list_of_coords       = [ (i,j)   for i in range(self._dim) 
                                                for j in range(self._dim)]

        # if user just give a number => init a random location of cells 
        if isinstance(self._init_cells, int) : 
            self._cells             = random.sample(    self.__list_of_coords, 
                                                        self._init_cells)
            self._init_cells        = self._cells

        # elif it is a list transform user cells in game's cells
        elif isinstance(self._init_cells, list) : 
            self._cells             = self._init_cells

        # record each cells of last round and last of last round
        # to be able to recognize 2 same states of the game 
        self.__last_cells           = self._cells
        self.__2last_cells          = self._cells

        # init game_state 
        self._state            = (self._round, self._cells, 0) 

        self.__start_called = False


    # properties : no comments no docstrings

    @property
    def round(self):
        return self._round


    @property
    def max_round(self):
        return self._max_round


    @property
    def init_cells_loc(self):
        return self._init_cells


    @property
    def init_cells_nb(self):
        return len(self._init_cells)


    @property
    def dim(self):
        return self._dim


    @property   
    def cells_loc(self):
        return self._cells


    @property   
    def waiter(self):
        return self._waiter


    @property   
    def auto_mode(self):
        return self._auto_mode


    @property   
    def cells_nb(self):
        return len(self._cells)


    @property   
    def state(self):
        return self._state
    

    @property   
    def space(self):
        """this is the UI game representation of the 'space' 
        
        positional args     : -
        optional args       : -
        do                  : -
        return              : return a specific str to represtent the "game's 
                              space"
        raise               : - 
        """

        txt = "\n"*2

        # game representation / space
        # use pandas.to string, but without indexes and columns' name
        s   = self._space.to_string(index=False, header=False)
        # replace 0 and 1 with readable values
        s   = s.replace("0", self.__DEAD_CELL).replace("1", self.__LIVING_CELL)
        # add a und the sapce to see it 
        s   = s.replace("\n", "|\n|")
        s   +="|\n" 
        s   = "\n|"+s
        s   = "---" * self.dim + s + "---" * self.dim +"\n"

        txt +=  s
        txt += "\n"

        # add game variables 
        txt +=  "round       =  {}\n".format(self.round)
        txt +=  "cells       =  {}\n".format(self.cells_nb)
        txt +=  "\n" *2

        # add game constants
        txt +=  "dim         =  {}\n".format(self.dim)
        txt +=  "max_round   =  {}\n".format(self.max_round)
        txt +=  "init_cells  =  {}\n".format(self.init_cells_nb)
        txt +=  "\n"*2

        # quit if needed
        txt +=  "press <Crlt + Z> to quit"
        txt +=  "\n"*2
        
        return txt


    def __str__(self) : 
        """just overwrite the __str__ method """
        
        return self.space


    # def __repr__(self) : 
    #   return self.space


    def neighbours_nb(self, i, j):
        """for the cell at coord (i,j) give the num of living neighbours 
        (min 0, max 8)"""

        return self.__neighbours_alive(i,j)


    def neighbours_loc(self, i,j) : 
        """for the cell at coord (i,j) give the coords (k,l) of living 
        neighbours"""

        return self.__neighbours_coords(i,j)


    def __build_default_space(self) : 
        """private method : build a space of self._dim ** 2 cells, will 
        all defualt values ie 0/dead
        
        positional args     : - 
        optional args       : -
        do                  : - 
        return              : type pd.DataFrame : empty dataframe (full of 0) 
                              of shape self.dim * self.dim
        raise               : - 
        """

        i = np.arange(self._dim)

        return(pd.DataFrame(0, index=i , columns=i))


    def __update_space(self) : 
        """private method :  incorporate cells from self._cells (list of coords 
        of living cells in game's space representation

        positional args     : - 
        optional args       : -
        do                  : update self._space with self._cells location as 1     
        return              : - 
        raise               : - 
        """

        # reset an empty space  in a tmp var    
        new_space = self.__build_default_space()

        # replace 0 with 1 if cell in self._cells list 
        for i,j in self._cells : 
            new_space.loc[i,j] = 1 

        # update _space
        self._space = new_space


    def __neighbours_alive(self, i,j) : 
        """private method : count how many living cells in the neighbourhood 
        of one cell 

        positional args     : int i, int j wich stands for y and x coords of 
                              a specific cell
        optional args       : -
        do                  : - 
        return              : an int as the number of living neighbours
        raise               : - 
        """

        neighbours = list()
        
        for (i,j) in self.__neighbours_coords(i,j) : 
            if self._space.iloc[i,j] == 1 : 
                neighbours.append(1)
        
        return len(neighbours)


    def __neighbours_coords(self, i,j)  : 
        """private method : give all possible coords of direct neihbourhood 
        for one cell

        positional args     : int i, int j wich stands for y and x coords of 
                              a specific cell
        optional args       : -
        do                  : - 
        return              : type list : list of tuples (y,x) as coords of 
                              existing neighbours
        raise               : - 
        """

        candidates = [  (i+1, j+1), (i-1, j-1),
                        (i+1, j-1), (i-1, j+1),
                        (i, j-1), (i, j+1),
                        (i+1, j), (i-1, j)  ]

        li = [(i,j) for (i,j) in candidates if (i,j) in self.__list_of_coords]

        return li


    def __update_cells(self) :  
        """private method : update for each cell, regarding the neighbourhood 
        and game's rules, if a cell change of  state (living/dead) or 
        stay alive/dead

        rules : if alive with 2/3 neighbours also alive : keep living, 
                else is killed 
                if dead with 3 neighbours alive: wake up and live else stay dead

        positional args     : - 
        optional args       : -
        do                  : update self._cells with live/die rules of the game    
        return              : - 
        raise               : - 
        """

        # create 2 empty list of cells, one to add and one to dell 
        add_cells   = list()
        del_cells   = list()
        
        # considering living cells 
        for i,j in self.__list_of_coords :
            # count how many neighbours  
            neighbours = self.__neighbours_alive(i,j)

            # if 2 or 3 neighbours --> stay alive 
            if (i,j) in self._cells : 
                if (neighbours == 2) or (neighbours == 3) : 
                    pass
                # if less or more --> die 
                else :
                    del_cells.append((i,j))

            # considering dead cells  
            else : 
                # if 3 neighbours --> wake up and live
                if neighbours == 3 : 
                    add_cells.append((i,j))
                else :
                    # else stay dead
                    pass

        # copy _cells in a tmp var
        new_cells = list(self._cells)

        # from living cells : delete cells who die 
        
        # -------------------------------------
        # -- > use list comprehension
        # -------------------------------------

        for (i,j) in self._cells : 
            if (i,j) in del_cells : 
                new_cells.remove((i,j))

        # with list of next living cells extend the curent list 
        new_cells.extend(add_cells)

        # update good attribute
        self._cells = new_cells


    def __detect_no_lives(self) : 
        """private method : if numb of living cells == 0, then  stop the game

        positional args     : -
        optional args       : -
        do                  : print out specific message
        return              : True if no cells alive, else False 
        raise               : - 
        """

        if not self._cells  : 
            end_no_lives()
            return True
        
        return False


    def __detect_last_round(self) : 
        """private method : if max_round stop the game

        positional args     : -
        optional args       : -
        do                  : print out specific message
        return              : True if game's max iteration reached (ie 
                              self._max_round) else False 
        raise               : - 
        """

        if self._round == self._max_round : 
            end_last_round()
            return True
        
        return False


    def __detect_game_fixed(self, arg) : 
        """private method : eval if game fixed ie the game will not evol due to 
        stablized structures (behive, block etc etc...)
        
        positional args     : the cells list to compare to self._cells 
        optional args       : -
        do                  : -
        return              : True if game's is fixed, 
                              else False 
        raise               : - 
        """

        if len(arg) == len(self._cells) : 
            for i in  arg : 
                if i not in self._cells : 
                    return False
            end_game_fixed()
            return True
        else : 
            return False


    def __update_state(self) : 
        """private method : regarding self._cells, self.max_round, (etc etc) 
        define if games has to stop or not 
        
        positional args     : -
        optional args       : -
        do                  : update self._state with self._round, 
                              self.cells_nb,  and status (ie __EXIT_STATUS)
        return              : - 
        raise               : -
        """

        if self.__detect_no_lives() : 
            self._state =  (self.round, self.cells_nb, 1)
        
        elif self.__detect_last_round() : 
            self._state =  (self.round, self.cells_nb, 2)
        
        elif self.__detect_game_fixed(self.__last_cells) : 
            self._state =  (self.round, self.cells_nb, 3)
        
        elif self.__detect_game_fixed(self.__2last_cells) : 
            self._state =  (self.round, self.cells_nb, 4)
        
        else : 
            self._state =  (self.round, self.cells_nb, 0)


    def __looper(self) : 
        """private method : find here the 'looper' method which is used to 
        deal with auto_mode True/False

        record last_cells and 2_last_cells to track fixed structures
        and increment self._round
        
        positional args     : -
        optional args       : -
        do                  : handle user interface for next iteration if needed,
                              update self._round, self.__last_cells and 
                              self.__2last_cells,  
        return              : - 
        raise               : - 
        """

        # if auto_mode just sleep a certain time 
        if self._auto_mode : 
            time.sleep(self._waiter)

        # else ask to user input before continuing
        else : 
            input(  "press <Enter>    to continue\n"
                    "press <Crlt + Z> to quit \n")

        # incremenent round
        self._round+=1

        # record last list of cells for dectecting fixed game (periodicity of 1)
        self.__last_cells = self._cells
        
        # record lastof last  list of cells for dectecting fixed game (periodicity of 2)        
        if self._round %2 : 
            self.__2last_cells = self._cells


    def _start(self) : 
        """first game representation for user 

        positional args     : -
        optional args       : -
        do                  : update self._space and print it, ask user input 
                              to start 
        return              : - 
        raise               : - 
        """

        self.__start_called = True 

        os.system("clear")
        game()

        # game repr
        self.__update_space()
        print(self.space)
        
        # user input 
        print("press <Enter>    to start")
        input("press <Crlt + Z> to quit\n") 


    def _next(self) :
        """update game's state and show game repr for each round

        positional args     : -
        optional args       : -
        do                  : update self._cells, self._space, self._state 
                              and print self._space 
        return              : - 
        raise               : - 
        """

        # header + game title
        os.system("clear")
        game()

        # update _cells and _space
        self.__update_cells()
        self.__update_space()
        
        # print game repr
        print(self.space)

        # update _state and call __looper if needed
        self.__update_state()
        # if exit status == 0 call __looper() 
        if not self._state[2] :                
            self.__looper()



    def run(self) : 
        """main method of the game, control strat, loop and exit values of a game
        
        positional args     : -
        optional args       : -
        do                  : call self._start(), then loop on self._next(),  
                              detect if game exit conditions and return
                              self._state if needed to break the loop
        return              : 3 dim tuple with self._round, self.cells_nb and 
                              exit status   
        raise               : - 
        """

        # initial state before starting game
        if not self.__start_called : 
            self._start()

        # main loop 
        while True : 

            # call next to upate game's parmas  
            self._next()

            # control game state
            if self._state[2] : 

                # if scenario occuring return 3 dim tupple
                return self._state


