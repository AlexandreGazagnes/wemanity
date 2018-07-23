#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
display.py
"""


"""
find here all print functions organized in master level (intro for exemple), 
and various title/subtitles levels (header for exemple)

even if it is a little 'overkilled', it is better to have all this features 
in the same module

see various comments and doctring for more information
"""


# import 

import os, logging


# functions


def intro() : 
    """basic welcome screen with print of instructions to stdout

    positional args     : - 
    optional args       : -
    do                  : print out welcome message     
    return              : -
    raise               : - 
    """

    os.system("clear")

    welcome()
    print("\n\n")

    msg="The game is a zero-player game, meaning that its evolution is determined\n"+\
        "by its initial state, requiring no further input. One interacts with\n"+\
        "the Game of Life by creating an initial configuration and observing how it\n"+\
        "evolves, or, for advanced players, by creating patterns with particular\n"+\
        "properties.\n"

    print(msg)

    input("press <Enter> to continue...\n") 


def close() : 
    """basic bye screen with print of an ending message to stdout

    positional args     : - 
    optional args       : -
    do                  : print out ending message  
    return              : -
    raise               : - 
    """

    input("\n\npress <Enter> to end the program...\n\n")

    os.system("clear")

    end()

    msg = str(  "\n\n"
                "#########################################\n"
                "\n"
                "              bye bye bye !!!             \n"
                "\n"
                "#########################################\n"
                "\n")

    print(msg)


def header() : 
    """basic header title called by every display's print function

    positional args     : - 
    optional args       : -
    do                  : print out an 'header' to have a fancy UI
    return              : -
    raise               : - 
    """

    msg = str(  "#########################################\n"
                "\n"
                "              GAME OF LIFE               \n"
                "\n"
                "#########################################\n"
                "\n\n")

    print(msg)


def options() : 
    """basic subtitle called by every arg_manager UI

    positional args     : - 
    optional args       : -
    do                  : print out an subtitle and header to have a fancy UI
    return              : -
    raise               : - 
    """

    header()

    msg =   "              OPTIONS\n"+\
            "_________________________________________\n"

    print(msg)


def game() : 
    """basic subtitle called by every GameOfLife._start or GameOfLife._next UI

    positional args     : - 
    optional args       : -
    do                  : print out an subtitle and header to have a fancy UI
    return              : -
    raise               : - 
    """

    header()

    msg =   "                GAME\n"+\
            "_________________________________________\n"

    print(msg)


def welcome() : 
    """basic subtitle called by intro in the GameOfLife.__init__ UI

    positional args     : - 
    optional args       : -
    do                  : print out an subtitle and header to have a fancy UI
    return              : -
    raise               : - 
    """

    header()

    msg =   "              WELCOME\n"+\
            "_________________________________________\n"

    print(msg)


def end() : 
    """basic subtitle called by close for the last screen of game's UI

    positional args     : - 
    optional args       : -
    do                  : print out an subtitle and header to have a fancy UI
    return              : -
    raise               : - 
    """

    header()

    msg =   "              END\n"+\
            "_________________________________________\n"

    print(msg)


def end_no_lives() : 

    msg =   "--------------------------------------------\n"    +\
            "         END --> no more cells living\n"           +\
            "--------------------------------------------\n"    +\
            "\n" * 2

    print(msg)
    close()


def end_last_round() : 

    msg =   "--------------------------------------------\n"    +\
            "        END --> maximum round reached\n"           +\
            "--------------------------------------------\n"    +\
            "\n" * 2

    print(msg)
    close()


def end_game_fixed() : 

    msg =   "--------------------------------------------\n"    +\
            "END --> gamed fixed no more evol can happend\n"    +\
            "--------------------------------------------\n"    +\
            "\n" * 2

    print(msg)
    close()
