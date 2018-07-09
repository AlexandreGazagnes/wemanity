#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
argparse.py
"""



# Find here argparse.py, wich is a short script to handle and manage CLI
# args when a program is launched. 

# This script is was written without importing argparse - seems to be too easy 
# for this question


# import

import sys, logging, os	


# logging

l = logging.INFO
logging.basicConfig(level=l, format='%(levelname)s : %(message)s')



def argparse(args=None) : 
	"""main function, please https://codingdojo.org/kata/Args/ for more info

	positional args     : - 
	optional args       : 'args'- for tests only - a string wich simulate the CLI arguments
	                      for a 'normal' usage of the package please just call argparse()
	return              : List or Dict with typed ans casted args
	raises              : TypeError if -l is not an int
	                      NotADirectoryError if -d is not a directory
	"""

	# extract user args
	if not args : 	
		user_args = sys.argv[1:]
	else : 
		if isinstance(args, str) : 	
			user_args = args.split(" ")[1:]
		else : 
			raise TypeError("TESTING args :{} - type error"
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
		raise TypeError(	"arg: -p, val :{} - type error"
									" : expected a < int >,"
									" recieved a < {} >".format(p, type(p)))

	d = dict_args["d"]
	
	if not os.path.exists(d): 
		raise NotADirectoryError(	"arg: -d, val: {} - "
									"invalid path".format(d))

	# basic logging
	logging.info(dict_args)

	return dict_args


# main	

def main() : 

	return argparse()


if __name__ == '__main__':
	main()

