# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise to print out to the console a number of specified 6-sided dice averaged together.
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
"""
import random

def get_number_dice():
	"""
	Asks the user for a number of 6 sided dice to roll
	:returns: The number of dice to roll as an integer
	"""
	print('Please input number of 6 sided dice to average ')
	return int(input())

def get_dice_sum(dice_rolled):
	"""
	Purpose: Get the dice sum
	:param 1: dice_rolled is the dice that was rolled as a list
	:returns: The dice sum as an integer
	"""
	total_sum = 0
	while 0 < len(dice_rolled):
		dice = random.randint(1, 6)
		total_sum += dice # total up the dice rolled
		total_dice -= 1
	return total_sum

def get_dice_rolled(number_dice_to_roll):
	"""
	Gets the dice that was rolled.
	:param 1: number_dice_to_roll is the number of dice to roll as an integer
	:returns: The each dice that was rolled as a list
	"""
	dice_rolled = []
	while 0 < number_dice_to_roll:
		dice_rolled.append(random.randint(1, 6))
	return dice_rolled

def calculate_mean(dice_sum, number_of_dice):
	"""
	Calculates the mean average of the dice that was rolled.
	:param 1: Total dice summed together as an integer
	:param 2: Number of dice that was rolled as integer
	:returns: Mean/average calculation as interger
	"""
	return int(dice_sum/number_of_dice)

def print_dice_rolled(dice_rolled):
	"""
	Prints the dice that was rolled to the console
	:param 1: The dice that was rolled as a list
	"""
	dice_output = ''
	for dice in dice_rolled:
		dice_output = dice_output + ' {}'.format(dice)
	print('The dice that was rolled was {}'.format(dice_output))

def print_dice_mean(dice_mean):
	"""
	Prints the dice mean to the standard console out
	:param 1: The mean/average of the rolled dice as an integer
	"""
	print('The mean of the dice that was rolled was: {}'.format(dice_mean))

def main():
    total_dice = get_number_dice()
    dice_rolled = get_dice_rolled(total_dice)
    dice_sum = get_dice_sum(dice_rolled)
    dice_mean = calculate_mean(dice_sum, total_dice)
    print_dice_rolled(dice_rolled)
    print_dice_mean(dice_mean)

if __name__ == "__main__":
    sys.exit(int(main() or 0))