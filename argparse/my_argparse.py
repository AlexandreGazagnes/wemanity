#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
argparse.py
"""


"""
Please find here my work about argparse kata code.
my_argparse.py is a module with one function 'my_parser', which is a parser 
for CLI arguments. 
In this work, I choose to not import the magic package named 'argparse'
which provide a full and fancy framework to handle CLI arguments, considering
that it would be a cheating way for answering to the problem, so you will find 
a CLI arguments parser designed at purpose 'from scratch'.
"""

# import

import sys, logging, os 


# logging

l = logging.WARNING
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')



def my_parser(args=None) : 
    """main function, please https://codingdojo.org/kata/Args/ for more info

    positional args     : - 
    optional args       : 'args'- for tests only - a string which simulate 
                           the CLI arguments - for a 'normal' use of the package
                           please just call my_parser()
    return              : type List or Dict with typed and casted args
    raises              : TypeError if -l is not an int
                          TypeError if args not a str - tests only
                          NotADirectoryError if -d is not a directory
    """

    # extract user args
    if not args :   
        user_args = sys.argv[1:]
    else : 
        if isinstance(args, str) :  
            user_args = args.split(" ")[1:]
        else : 
            raise TypeError(    "TESTING args :{} - type error"
                                " : expected a < str >,"
                                " recieved a < {} >".format(args, type(args)))

    # basic logging
    logging.info(user_args)

    # create a container to return
    dict_args = dict(l=False, p=0, d="")

    # log
    if "-l" in user_args : 
        dict_args["l"] = True
    
    # port 
    if "-p" in user_args  : 
        dict_args["p"] = user_args[1 + user_args.index("-p")]
    
    # directory
    if "-d" in user_args  : 
        dict_args["d"] = user_args[1 + user_args.index("-d")]

    # basic logging
    logging.info(dict_args)

    # check if args are goods : 
    p = dict_args["p"]

    try:
        dict_args["p"] = int(dict_args["p"])
    except :
        p = dict_args["p"]
        raise TypeError(    "arg: -p, val :{} - type error"
                            " : expected a < int >,"
                            " recieved a < {} >".format(p, type(p)))

    d = dict_args["d"]
    
    if ((not os.path.exists(d)) and (d) ): 
        raise NotADirectoryError(   "arg: -d, val: {} - "
                                    "invalid path".format(d))

    # basic logging
    logging.info(dict_args)

    return dict_args


# main  

def main() : 

    return my_parser()


if __name__ == '__main__':
    main()

