# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Farckle Dice Roll game exercise
by Matthew James K
Instructions:
Write a program that scores a single roll of Farkle. Roll 5 6-sided dice.
Three 1s are worth 1000 points.
Three 2s are worth 200 points.
Three 3s are worth 300 points.
Three 4s are worth 400 points.
Three 5s are worth 500 points.
Three 6s are worth 600 points.
Any remaining 1s are worth 100 points each.
Any remaining 5s are worth 50 points each.
Advanced:
Allow re-rolling of any of the dice and re-calculate the score. Figure out a way to have the user select which dice to re-roll.
Implement multiple rolls as per the full turn rules.
Full Turn Rules:
Player starts by rolling all the dice.
If the player ever rolls any number of dice and scores 0 with those dice, they have Farkled, lose all their points for this turn, and are done.
After each roll, the player must set aside at least one die that scores. They can set aside as many as they want.
Scoring is per-roll. Dice can't be combined between rolls to make bigger combos.
They player can decide to re-roll with any dice not set aside for scoring. If they don't re-roll, they stop and keep all their scored points.
If the player can set aside all dice as scoring dice, then their score for this turn is saved and they can start again with all five dice! If they Farkle, they still get 0 for the turn.
Super Advanced:
Implement a whole game with multiple players as per the whole game rules.
Whole Game Rules:
Each player has a turn in order.
A player may always start their turn from 0 points and roll all of the dice.
Also, if the player before them stopped without Farkling, this player may roll just the non-scoring dice and "piggy back" on the previous score.
Check out https://en.wikipedia.org/wiki/Farkle.
"""
import random
dice = dict({'1':0, '2':0, '3':0, '4':0, '5':0})
rolled = dict({'1':0, '2':0, '3':0, '4':0, '5':0, '6':0})
total_score = 0
print('Press enter to start rolling 5 dice... or \'d\' for done.')

accept_input = True;
while accept_input:
	continue_answer = input()
	if 'd' == continue_answer:
		accept_input = False
		continue
	
	for dicekey in dice:
		if 0 == dice[dicekey]:
			dice[dicekey] = int(random.randint(1, 6))

	for die in dice.values():
		if 1 == die:
			rolled['1'] += 1
		elif 2 == die:
			rolled['2'] += 1
		elif 3 == die:
			rolled['3'] += 1
		elif 4 == die:
			rolled['4'] += 1
		elif 5 == die:
			rolled['5'] += 1
		elif 6 == die:
			rolled['6'] += 1

	dice = dict({'1':1, '2':1, '3':1, '4':5, '5':1})
	rolled = {'1': 4, '2': 0, '3': 0, '4': 0, '5': 1, '6': 0} #debugging this specified sequence as a test

	if 5 == rolled['1']:
		total_score += 1200
	if 4 == rolled['1']:
		total_score += 1100
	if 3 == rolled['1']:
		total_score += 1000
	if 2 == rolled['1']:
		total_score += 200
	if 1 == rolled['1']:
		total_score += 100
	if 3 == rolled['2']:
		total_score += 200
	if 3 == rolled['3']:
		total_score += 300
	if 3 == rolled['4']:
		total_score += 400
	if 3 == rolled['5']:
		total_score += 500
	if 3 == rolled['6']:
		total_score += 600
	if 5 == rolled['5']:
		total_score += 600
	if 4 == rolled['5']:
		total_score += 550
	if 2 == rolled['5']:
		total_score += 100
	if 1 == rolled['5']:
		total_score += 50

	if 0 == total_score:
		print('You farkled! No points this time, please try again.')
	else:
		print('Your total score was: ', total_score)
	print('The numbers rolled for each dice was: {} {} {} {} {}'.format(
		dice['1'], dice['2'], dice['3'], dice['4'], dice['5']))
	print('The score tabulation for this roll attempt was: {} 1\'s {} 2\'s {} 3\'s {} 4\'s {} 5\'s {} 6\'s'.format(
		rolled['1'], rolled['2'], rolled['3'], rolled['4'], rolled['5'], rolled['6']))
	print('Please specify which dice to re-roll: 1 for first dice or 2 for second dice separated by a space:')
	reroll = str(input())
	reroll = reroll.split(' ')
	for die_number in reroll:
		rolled[str(dice[die_number])] -= 1
		dice[die_number] = 0
# end while accept_input: