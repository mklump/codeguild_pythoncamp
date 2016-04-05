# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by Matthew James K
LAB/STEP requirements:

Practice: Blackjack Hand
Implement scoring a single hand of blackjack.
Cards have point values. Aces are 1 or 11, number cards are their number, face cards are all 10. A hand is worth the sum of all the points of the cards in it. An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.
	• Make a class that represents a card.
	• Make a class that represents a hand.
	• Add functions that adds a card to a hand, one that scores a hand, and one that returns if the score is over 21.
	• Allow a user to type in a hand and have it be converted into card objects and then scored.
"""

class Card:
    def __init__(self, point_value):
        """
        Single argument "magic" constructor
        """
        self.point_value = point_value

    def __repr__(self):
        """
        String definition representation of this object. 'this' instead of 'self' but are still the same.
        Prints out the point_value for this particular card.
        """
        return 'Card({0})'.format(
            self.point_value
            )

    def __eq__(self, other_card):
        """
        Overloaded == equality operator
        """
        return self.point_value == other_card.point_value

class Hand:
    def __init__(self, hand_of_cards_list):
        """
        Single argument "magic" constructor
        """
        if None == hand_of_cards_list:
            self.hand_of_cards_list = list(Card) # or [Card] to this init assignment should still work
        else:
            self.hand_of_cards_list = hand_of_cards_list

    def __repr__(self):
        """
        String definition representation of this object. 'this' instead of 'self' but are still the same.
        Prints out the point_value for this particular card.
        """
        return 'Hand({0})'.format(self.hand_of_cards_list)

    def __eq__(self, other_hand):
        for card in range(len(self.hand_of_cards_list)):
            if self.hand_of_cards_list[card] != other_hand.hand_of_cards_list[card]:
                return False
        #end for checking
        return True