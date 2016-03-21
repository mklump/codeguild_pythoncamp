# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise to print out to the console a number of specified 6-sided dice averaged together.
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
"""
import random

def get_number_dice():
	print('Please input number of 6 sided dice to average ')
	return int(input())

def get_dice_sum(total_dice = 0):
	total_sum = 0
	while 0 < total_dice:
		dice = random.randint(1, 6)
		total_sum += dice
		total_dice -= 1
		print(total_dice, 'dice left to roll, and the value is', dice, '.')
	return total_sum

total_dice = get_number_dice()
print('The average or mean of all die rolls is ', int(get_dice_sum(total_dice)/total_dice))
