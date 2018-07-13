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

	welcome()
	print("\n\n")

	msg="The game is a zero-player game, meaning that its evolution is determined\n"+\
		"by its initial state, requiring no further input. One interacts with\n"+\
		"the Game of Life by creating an initial configuration and observing how it\n"+\
		"evolves, or, for advanced players, by creating patterns with particular\n"+\
		"properties.\n"

	print(msg)

	input("press <Enter> to continue...\n")	

	return 0


def close() : 

	"""basic bye screen with print out ending message to stdout

	positional args  	: - 
	optional args 		: -
	do 					: print out ending message 	
	return 				: 0 
	raises				: - 
	"""

	logging.info("close() called")

	input("\n\npress <Enter> to end the program...\n\n")

	os.system("clear")

	end()

	msg = str(	"\n\n"
				"#########################################\n"
				"\n"
				"              bye bye bye !!!             \n"
				"\n"
				"#########################################\n"
				"\n")

	print(msg)

	return 0


def header() : 

	msg = str(	"#########################################\n"
				"\n"
				"              GAME OF LIFE               \n"
				"\n"
				"#########################################\n"
				"\n\n")

	print(msg)




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


