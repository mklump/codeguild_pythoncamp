# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise to ask to a secret number between 1 and 10, then try to guess the secret number in 3 tries.
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
"""
import random

def print_secret_number_annoucement():
	"""
	Prints to concole standard out a secret number caculation as begun, then pauses to continue
	"""
	print('I have a secret number between 1 and 10, guess higher or lower.')
	input()

def get_secret_number():
	"""
	Returns the a random secret number between 1 and 10
	:returns: The secret number after asking for it
	"""
	return random.randint(1, 10)

def guess_number():
	"""
	Prompts the user for a number to guess from console standard in
	"""
	print('Guess? ')
	guess = int(input())

def is_higher(guess, secret):
	"""
	True if the guess number is higher, otherwise False
	:returns: True if secret is higher than guess, otherwise False
	"""
	return guess < secret

def is_lower(guess, secret):
	"""
	True if the guess number is lower, otherwise False
	:returns: True if secret is lower than guess, otherwise False
	"""
	return guess > secret

def print_guesses(number_guesses, secret):
	"""
	Prints to console standard out result of each guess
	:param 1: number_guesses remaining from the previous call of this function as an integer
	:param 2: secret number to check against with as an integer
	:returns: number_guesses remaining from previous call as an integer
	"""
	while secret != guess and number_guesses > 0:
		guess = guess_number()
		if is_higher(guess, secret):
			print('My secret number is higher.')
		elif is_lower(guess, secret):
			print('My secret number is lower.')
		number_guesses -= 1
		print('You have ', number_guesses, ' remaining!')
		return number_guesses

def process_guesses(number_guesses, secret):
	"""
	Performs the loop logic for each of the guesses
	:param 1: number_guesses is the number of guesses remaining as an integer
	:param 2: secret is the number being guessed as an integer 1 to 10
	:returns: number_guesses remaining from previous call as an integer
	"""
	while 0 < number_guesses:
		number_guesses = print_guesses(number_guesses, secret)
	return number_guesses

def print_guesses_output(number_guesses, secret):
	"""
	Prints the result of each guess to console standard out
	:param 1: number_guesses is the number of guesses remaining as an integer
	:param 2: secret is the number being guessed as an integer 1 to 10
	"""

def main():
    number_guesses = 3
    print_secret_number_annoucement()
    secret = get_secret_number()
    if 0 == numGuesses:
        print('No more guesses remaining.')
    elif 0 < numGuesses and secret == guess:
        print('You found my secret number!')

if __name__ == "__main__":
    sys.exit(int(main() or 0))