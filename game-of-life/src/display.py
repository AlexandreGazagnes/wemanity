#!/usr/bin/env python3
#-*- coding: utf8 -*-


"""
display.py
"""


"""
Find here all print functions organized in master level (intro for exemple), and various sub levels (header for exemple)
even if it is a little overkilled, it is better to have all this features in the same module
see various comments and doctring for more information
"""


# import 

import os, logging


# functions

def intro() : 
	"""basic welcome screen with print out instcuctions to stdout

	positional args  	: - 
	optional args 		: -
	do 					: print out welcome message 	
	return 				: 0 
	raises				: - 
	"""

	logging.info("intro() called")

	os.system("clear")

	msg = str(	"#########################################\n"
				"\n"
				"              GAME OF LIFE               \n"
				"\n"
				"#########################################\n"
				"\n\n")

	print(msg)

	return 0


def close() : 

	"""basic bye screen with print out ending message to stdout

	positional args  	: - 
	optional args 		: -
	do 					: print out ending message 	
	return 				: 0 
	raises				: - 
	"""

	logging.info("closeo() called")



	msg = str(	"#########################################\n"
				"\n"
				"              bye bye bye !!!             \n"
				"\n"
				"#########################################\n"
				"\n\n")

	print(msg)

	return 0





def options() : 

	header()

	msg = 	"              OPTIONS\n"+\
			"_________________________________________\n"

	print(msg)


def game() : 

	header()

	msg = 	"                GAME\n"+\
			"_________________________________________\n"

	print(msg)


def welcome() : 

	header()

	msg = 	"              WELCOME\n"+\
			"_________________________________________\n"

	print(msg)


def end() : 

	header()

	msg = 	"              END\n"+\
			"_________________________________________\n"

	print(msg)


def end_no_lives() : 

	msg = 	"--------------------------------------------\n"+\
			"         END --> no more cells living\n"   +\
			"--------------------------------------------\n"+\
			"\n" * 2

	print(msg)
	close()


def end_last_round() : 

	msg = 	"--------------------------------------------\n"+\
			"        END --> maximum round reached     \n"   +\
			"--------------------------------------------\n"+\
			"\n" * 2

	print(msg)
	close()


def end_game_fixed() : 

	msg = 	"--------------------------------------------\n"+\
			"END --> gamed fixed no more evol can happend    \n"   +\
			"--------------------------------------------\n"+\
			"\n" * 2

	print(msg)
	close()


