# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise select a hidden word from a predefined TUPLE list, and attempt to guess the hidden word
in the form of a hangman game.
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
Requirements to perform step by step:
1) Select a predefined word from a tuple imutable ordered sequence datastructure
2) Show the user blank signs (_ underscore character) for every letter not guessed
3) Show the user correctly guessed letters by filling in each correctly guessed space
4) Show the user previously guesses incorrect letters
5) Limit the maximum number of guessed letters to six (6) hard coded
6) Let the user enter each new letter
7) Can only make six (6) missed guesses, then reveal the remaining correct answers
word: _A_
wrong: B
mistakes remaining: 5
"""
import os
import sys
import random

def game_intro():
	"""
	Prints out to standard out an introduction for the game startup
	"""
	print('In this version of Hangman: I have a secret word, and you get 6 guesses before I must reveal.')
	print('Press enter to continue:')
	input()

def print_notguessed(guessed):
	"""
	Prints to console standard out the words not guessed of the specified word being guessed
	:param 1: guessed is letters of the secret word guessed and also not guessed for printing
	"""
	print('word: {}'.format(guessed))

def print_guessed(word, remaining):
	"""
	Prints to console standard out the letter correctly guessed of the specified word being guessed
	:param 1: secret word not yet guessed as a string
	:param 2: remaining is characters of the secret word that have been revealed as a string
	"""
	return None

def print_wrongletters(guesswrong):
	"""
	Prints to console standard out the letters guessed wrong
	:param 1: guesswrong is a string type of capital letter not correctly guess in the secret word
	:returns: guesswrong string of letters not guessed correct
	"""
	print('wrong: {}'.format(guesswrong))
	return guesswrong;

def print_mistakes(num_guess_remain):
	"""
	Prints to console standard out the number of remaining mistakes allowed before the secret word is revealed
	:param 1: num_guess_remain is the remaining number of guesses as integer
	"""
	print('mistakes remaining: {}'.format(num_guess_remain))

def get_random_word(word_tuple):
	"""
	Accepts a tuple of predefined words, and returns the selected random word
	:param 1: word_tuple is a data structure tuple of predefined words as a tuple
	:returns: the selected random word as a string
	"""
	word = random.choice(list(word_tuple))
	return word

def hide_secret_word(word):
	"""
	Takes the secret word as the word parameter, and hides all the characters using '_' based on the length of the word
	:param 1: word as the secret word to be hidden as a string
	:returns: secret hidden word as a string
	"""
	wordlist = list(word)
	for i in range(len(wordlist)): # Operation on a temporary list
		wordlist[i] = '_ '
	#for i in range(len(wordlist)): # Convert back to string return value
	#	hidden_word += '{} '.format(wordlist[i])
	hidden_word = ''.join(wordlist).strip()
	return hidden_word

def guess_letter():
	"""
	Prompt the user for a letter in the secret word at the console
	:returns: the guessed letter as a string
	"""
	Print('Enter a letter to guess:')
	return input()

def get_guesses(word, remaining):
	"""
	Processes guessing each letter - function may split again
	:param 1: secret word not yet guessed as a string
	:param 2: remaining is characters of the secret word that have been revealed as a string
	"""
	letter = guess_letter()
	for i in range(len(word)):
		if letter[i] == word[i]:
			letter[i] = word[i]
	raise NotImplementedError('This console program and the related refactoring are not yet completed (INIT/STUB->LOGIC->TEST->REPEAT)')

# begin main program/test
# raise NotImplementedError('This console program and the related refactoring are not yet completed (INIT/STUB->LOGIC->TEST->REPEAT)')
words_smalltuple = (
#'.NET',
'Agile',
#'AJAX',
#'Apache',
#'Apache Foundation',
#'API',
#'ASCII',
'bash'
#'bus numbers',
#'C',
#'C#',
#'C++',
#'cloud service',
)

game_intro()
secret_word = get_random_word(words_smalltuple)
hidden_word = hide_secret_word(secret_word)
get_guesses(secret_word, hidden_word)
# end main program/test

words_largetuple = (
'.NET',
'Agile',
'AJAX',
'Apache',
'Apache Foundation',
'API',
'ASCII',
'bash',
'bus numbers',
'C',
'C#',
'C++',
'cloud service',
'client-side language',
'client-server architecture',
'Clojure',
'console interface',
'cookies',
'CouchDB',
'CPython',
'Cython',
'Django',
'Docker',
'docstrings',
'Document Object Model (DOM)',
'event driven programming',
'event loop',
'Extreme Programming (XP)',
'filesystem',
'Flask',
'Food Cart Pod',
'FTP',
'garbage collection',
'Git',
'graph',
'GUI',
'HTML / CSS',
'HTTP',
'HTTPS',
'IDE',
'IDLE',
'IronPython',
'Java',
'JavaScript',
'JQuery',
'JuJu',
'JVM',
'Jython',
'LAMP',
'LIFO',
'Linux',
'Mono',
'MongoDB',
'MySQL',
'NNTP',
'Node.js',
'noSQL',
'ORM',
'POSIX',
'PostgreSQL',
'Python Enhancement Proposal (PEP)',
'Planet Python',
'protocol',
'Pycon',
'Python',
'python.org',
'Python Software Foundation (PSF)',
'queue',
'REPL',
'RSA',
'scala',
'server-side language',
'SMTP',
'Structured Query Language (SQL)',
'stack',
'symmetric key',
'tcl',
'TCP / IP',
'thick vs thin client',
'Tk',
'tree',
'Ubuntu',
'Unicode',
'VCS',
'version control',
'virtual machine',
'wiki',
'web browser',
'XML'
)