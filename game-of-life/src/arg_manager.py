#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
arg_manager.py
"""


"""
find here all arguments manager instructions
ie arg_manager is the main function,which  will be called or not manualy by 
the user and will be (re)called by GameOfLife.__init__()

arg_manager will handle manual UI to input args ("ask") and also auto check ("check")
all args to validate type, value etc etc

this arg_manager could become a class in the next version, just to increase 
code readability and to force user's iputs to be submited to a hidden check 
function

see various docstrings bellow for more information
"""


# import 

import os, sys, argparse, logging
from src.consts import *
from src.display import *


# functions

def arg_manager(options_dict=None) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    if not isinstance(options_dict, dict) : 

        options_dict = dict()


    options = dict( dim         = None,
                    auto_mode   = None,
                    waiter      = None, 
                    max_round   = None, 
                    init_cells  = None,     )


    if "dim" in options_dict.keys() : 
        if check_dim(options_dict["dim"]) : 
            options["dim"] = options_dict["dim"]
        else : 
            options["dim"] = ask_dim()
    else : 
        options["dim"] = ask_dim()

    if "auto_mode" in options_dict.keys() : 
        if check_auto_mode(options_dict["auto_mode"]) : 
            options["auto_mode"] = options_dict["auto_mode"]
        else : 
            options["auto_mode"] = ask_auto_mode()
    else : 
        options["auto_mode"] = ask_auto_mode()

    if options["auto_mode"] : 
        if "waiter" in options_dict.keys() : 
            if check_waiter(options_dict["waiter"]) : 
                options["waiter"] = options_dict["waiter"]
            else : 
                options["waiter"] = ask_waiter()
        else : 
            options["waiter"] = ask_waiter()

        if "max_round" in options_dict.keys() : 
            if check_max_round(options_dict["max_round"]) : 
                options["max_round"] = options_dict["max_round"]
            else : 
                options["max_round"] = ask_max_round()
        else : 
            options["max_round"] = ask_max_round()

    else : 
        options["waiter"]       = WAITER_DEFAULT
        options["max_round"]    = MAX_ROUND_MAX


    if "init_cells" in options_dict.keys() : 
        if check_init_cells(options_dict["init_cells"], options["dim"]) : 
            options["init_cells"] = options_dict["init_cells"]
        else : 
            options["init_cells"] = ask_init_cells(options["dim"])
    else : 
        options["init_cells"] = ask_init_cells(options["dim"])

    return options



# def arg_builder() : 
#   """ """

#   pass


def default_args() : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    logging.info("default_args() called")

    options = dict(     dim         = DIM_DEFAULT, 
                        init_cells  = INIT_CELLS_DEFAULT, 
                        auto_mode   = AUTO_MODE_DEFAULT,
                        waiter      = WAITER_DEFAULT,
                        max_round   = MAX_ROUND_DEFAULT)

    check_options(options) 

    return options


def check_options(options) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    check_dim(options["dim"])
    check_waiter(options["waiter"])
    check_auto_mode(options["auto_mode"])
    check_max_round(options["max_round"])
    check_init_cells(options["init_cells"], options["dim"])


def ask_dim() : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    msg =   "\n\n" + \
            "please choose the dimension of games's space : \n\n" + \
            "\texpected an {} with min {} and max {} \n".format(type(DIM_MAX), DIM_MIN, DIM_MAX) + \
            "\teg dim = 3 will build a 3 * 3 space with 9 cases \n" + \
            "\tpress <Enter> for default value : {}\n".format(DIM_DEFAULT) + \
            "\tpress <Ctrl+Z> to quit \n" + \
            "\n"
    
    os.system("clear")

    options()

    while True : 

        dim = input(msg)

        if not dim : 
            return DIM_DEFAULT

        try : 
            dim = int(dim)
            if dim > DIM_MAX : 
                print("\n\ndim value error, expected max {}, recieved {}".format(DIM_MAX, dim))
            elif dim < DIM_MIN : 
                print("\n\ndim value error, expected min {}, recieved {}".format(DIM_MIN, dim))
            else : 
                return dim 
        except : 
            print("\n\ndim type error, expected {}, recieved {}".format(type(DIM_MAX),type(dim)))


def check_dim(dim) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    param = True
    if not isinstance(dim, int) : 
        param = False
        print("TypeError(dim type error, expected <class 'int'>, recieved {}".format(type(dim)))
    
    else : 
        if dim > DIM_MAX :
            param = False
            print("ValueError(dim value error, expected max {}, recieved {}".format(DIM_MAX, dim))

        if dim < DIM_MIN :
            param= False
            print("ValueError(dim value error, expected min {}, recieved {}".format(DIM_MIN, dim))

    decor_param(param)

    return param


def ask_auto_mode() : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """
    
    msg =   "\n\n" + \
            "please choose to enable or disable auto_mode : \n\n" + \
            "\texpected an 'y' for 'yes/True' or a 'n' for 'no/False' \n" + \
            "\tif auto_mode, iterations will be done automaitcly after a time waiter\n"+\
            "\tif not you will have to press < Enter > for each iteration  \n" + \
            "\tpress <Enter> for default value : {}\n".format(AUTO_MODE_DEFAULT) + \
            "\tpress <Ctrl+Z> to quit \n" + \
            "\n"
    
    os.system("clear")

    options()

    while True : 

        auto_mode = input(msg)

        if not auto_mode : 
            return AUTO_MODE_DEFAULT

        if auto_mode.lower().strip() == "y" : 
            return True

        elif auto_mode.lower().strip() == "n" :
            return False

        else :
            print("\n\nauto_mode error 'y' or 'n', recieved {}".format(auto_mode))


def check_auto_mode(auto_mode) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """
    
    param = True 
    if not isinstance(auto_mode, bool) : 
        param = False
        print("TypeError(auto_mode type error, expected <class 'bool'>, recieved {}".format(type(auto_mode)))

    decor_param(param)

    return param


def ask_waiter() : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    msg =   "\n\n" + \
            "please choose the refresh time value of the game : \n\n" + \
            "\texpected an {} in seconds with min {} and max {} \n".format(type(WAITER_MAX), WAITER_MIN, WAITER_MAX) + \
            "\tconsider waiter as the time between two iterations \n" + \
            "\tpress <Enter> for default value : {}\n".format(WAITER_DEFAULT) + \
            "\tpress <Ctrl+Z> to quit \n" + \
            "\n"
    
    os.system("clear")

    options()

    while True : 

        waiter = input(msg)

        if not waiter : 
            return WAITER_DEFAULT

        try : 
            waiter = float(waiter)
            if waiter > WAITER_MAX : 
                print("\n\refresh value error, expected max {}, recieved {}".format(WAITER_MAX, waiter))
            elif waiter < WAITER_MIN : 
                print("\n\refresh value error, expected min {}, recieved {}".format(WAITER_MIN, waiter))
            else : 
                return waiter 
        except : 
            print("\n\refresh type error, expected {}, recieved {}".format(type(WAITER_MAX), type(waiter)))


def check_waiter(waiter) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """
    
    param=True
    if not ((isinstance(waiter, int)) or (isinstance(waiter, float)) ): 
        param = False
        print("TypeError(waiter type error, expected <class 'int' / 'float'>, recieved {}".format(type(waiter)))

    else :  
        if waiter > WAITER_MAX :
            param=False     
            print("ValueError(waiter value error, expected max {}, recieved {}".format(WAITER_MAX, waiter))
        if waiter < WAITER_MIN :
            param = False
            print("ValueError(waiter value error, expected min {}, recieved {}".format(WAITER_MIN, waiter))

    decor_param(param)

    return param


def ask_max_round() : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    msg =   "\n\n" + \
            "please choose the max round number of the game : \n\n" + \
            "\texpected an {} with min {} and max {} \n".format(type(MAX_ROUND_MAX), MAX_ROUND_MIN, MAX_ROUND_MAX) + \
            "\tconsider max_round as a sanity check to avoid infinite loop or computational overholding\n" + \
            "\tpress <Enter> for default value : {}\n".format(MAX_ROUND_DEFAULT) + \
            "\tpress <Ctrl+Z> to quit \n" + \
            "\n"
    
    os.system("clear")

    options()

    while True : 

        max_round = input(msg)

        if not max_round : 
            return MAX_ROUND_DEFAULT

        try : 
            max_round = int(max_round)
            if max_round > MAX_ROUND_MAX : 
                print("\n\nmax_round value error, expected max {}, recieved {}".format(MAX_ROUND_MAX, max_round))
            elif max_round < MAX_ROUND_MIN : 
                print("\n\nmax_round value error, expected min {}, recieved {}".format(MAX_ROUND_MIN, max_round))
            else : 
                return max_round 
        except : 
            print("\n\nmax_round type error, expected {}, recieved {}".format(type(MAX_ROUND_MAX), type(max_round)))


def check_max_round(max_round) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    param = True
    if not isinstance(max_round, int) : 
        param = False
        print("TypeError(max_round type error, expected <class 'int'>, recieved {}".format(type(max_round)))

    else : 
        if max_round > MAX_ROUND_MAX :
            param = False
            print("raise ValueError(max_round value error, expected max {}, recieved {}".format(MAX_ROUND_MAX, max_round))
        if max_round < MAX_ROUND_MIN :
            param = False
            print("ValueError(max_round value error, expected min {}, recieved {}".format(MAX_ROUND_MIN, max_round))

    decor_param(param)

    return param


def ask_init_cells(dim) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    init_cells_max = int(0.75 * dim **2) 

    init_cells_default = int(0.4 * init_cells_max)

    msg =   "\n\n" + \
            "please choose the number of cells of the init state of the game: \n\n" + \
            "\texpected an {} with min {} and max {} \n".format(type(INIT_CELLS_DEFAULT), INIT_CELLS_MIN, init_cells_max) + \
            "\teg init_cells = 10 will build 10 cells randomly located at the begining of the game \n" + \
            "\tpress <Enter> for default value : {}\n".format(init_cells_default) + \
            "\tpress <Ctrl+Z> to quit \n" + \
            "\n"
    
    os.system("clear")

    options()

    while True : 

        init_cells = input(msg)

        if  not init_cells : 
            return init_cells_default

        try : 
            init_cells = int(init_cells)
            if init_cells > init_cells_max : 
                print("\n\ndim value error, expected max {}, recieved {}".format(init_cells_max, init_cells))
            elif init_cells < INIT_CELLS_MIN : 
                print("\n\ndim value error, expected min {}, recieved {}".format(INIT_CELLS_MIN, init_cells))
            else : 
                return init_cells 
        except : 
            if isinstance(init_cells, list) : 
                return init_cells
            else : 
                print("\n\ndim type error, expected {}, recieved {}".format(type(init_cells_max),type(init_cells)))


def check_init_cells(init_cells, dim) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    init_cells_max = int(0.75 * dim **2) 

    param = True

    if isinstance(init_cells, list) : 
        return True

    if not isinstance(init_cells, int) : 
        param = False
        print("TypeError(init_cells type error, expected <class 'int'>, recieved {}".format(type(init_cells)))
    
    else : 
        if init_cells > init_cells_max :
            param = False
            print("raise ValueError(init_cells value error, expected max {}, recieved {}".format(init_cells_max, init_cells))
        if init_cells < INIT_CELLS_MIN :
            param = False
            print("ValueError(init_cells value error, expected min {}, recieved {}".format(INIT_CELLS_MIN, init_cells))

    decor_param(param)

    return param


def decor_param(param) : 
    """return default argumennts

    positional args     : - 
    optional args       : - 
    return              : dict object with key/values of arguments 
    raises              : - 
    """

    if not param : 
        print("we will ask you to choose this parametre manualy :(\n")
        # input("press <Enter> to continue ...\n")

