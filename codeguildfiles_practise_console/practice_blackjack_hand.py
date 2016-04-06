# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by Matthew James K
LAB/STEP requirements:

Practice: Blackjack Hand
Implement scoring a single hand of blackjack.
Cards have point values. Aces are 1 or 11, number cards are their number, face cards are all 10. A hand is worth the sum of all the points of the cards in it. An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.
	Make a class that represents a card.
	Make a class that represents a hand.
	Add functions that adds a card to a hand, one that scores a hand, and one that returns if the score is over 21.
	Allow a user to type in a hand and have it be converted into card objects and then scored.
"""
import random

class Card:
    def __init__(self, card_type_of_thirteen, point_value, suite):
        """
        Three argument "magic" constructor
        """
        self.card_type_of_thirteen = card_type_of_thirteen
        self.point_value = point_value
        self.suite = suite

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
# end class Card:

class Hand:
    def __init__(self, hand_of_cards_list = []):
        """
        Single argument "magic" constructor
        """
        self.hand_of_cards_list = hand_of_cards_list #[Card] # or list(Card) if the collection is iterable to this init assignment should still work

    def __repr__(self):
        """
        String definition representation of this object. 'this' instead of 'self' but are still the same.
        Prints out the point_value for this particular card.
        """
        return 'Hand({0})'.format(self.hand_of_cards_list)

    def __eq__(self, other_hand):
        """
        Overloaded == equality operator
        """
        for card in range(len(self.hand_of_cards_list)):
            if self.hand_of_cards_list[card] != other_hand.hand_of_cards_list[card]:
                return False
        #end for checking
        return True

    def add_card_to_hand(self):
        """
        This class function adds a SINGLE Card object to the list(Card) collection and returns the modified list.
        :returns: The modified input list with the new added card just now drawn
        """
        #card_value_type = namedtuple('card_value_type', ('2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace'))
        #accessible through the dot operator such as card_value_type.2 or card_value_type.Jack or card_value_type.Ace

        next_card_drawn = Card(str(), 0, str())
        rand_pokercard_type = random.randint(1, 13)
        if 1 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '2'
            next_card_drawn.point_value = 2
        elif 2 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '3'
            next_card_drawn.point_value = 3
        elif 3 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '4'
            next_card_drawn.point_value = 4
        elif 4 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '5'
            next_card_drawn.point_value = 5
        elif 5 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '6'
            next_card_drawn.point_value = 6
        elif 6 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '7'
            next_card_drawn.point_value = 7
        elif 7 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '8'
            next_card_drawn.point_value = 8
        elif 8 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '9'
            next_card_drawn.point_value = 9
        elif 9 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = '10'
            next_card_drawn.point_value = 10
        elif 10 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = 'JACK'
            next_card_drawn.point_value = 10
        elif 11 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = 'QUEEN'
            next_card_drawn.point_value = 10
        elif 12 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = 'KING'
            next_card_drawn.point_value = 10
        elif 13 == rand_pokercard_type:
            next_card_drawn.card_type_of_thirteen = 'ACE'
            next_card_drawn.point_value = 11
        self.hand_of_cards_list.append(next_card_drawn)
        return self.hand_of_cards_list

    def score_this_hand(self, hand_of_cards_list = []):
        """
        This class function accepts the List() [] of Card objects of this self.hand_of_cards_list,
        and scores this particular Hand based on the card values drawn Card.point_value.
        :param 1: hand_of_cards_list as the card list of Hand instance member of all presently drawn cards in this hand
        :returns: The total score based on black jack rules for this Hand
        """
        current_points = 0
        for card in self.hand_of_cards_list:
            current_points += card.point_value
            if True == self.is_score_over_twentyone(current_points):
                self.print_score_busted()
        return current_points

    def is_score_over_twentyone(self, current_total_points):
        """
        This class function tests whether or not the current total score of this Hand is over 21, if it is then this
        fuction returns True, otherwise False.
        :returns: True if the score of this Hand.hand_of_cards_list is over 21, other wise False
        """
        return current_total_points > 21 #TODO: Test if ACE object is in the hand list, and change it to 1 if over 21!

    def print_score_busted(self):
        """
        This class function prints to standard out a message when the total score busts the 21 limit.
        """
        print('You busted with your score over 21!')
# end class Hand:

    def prompt_the_user_to_input_a_hand():
        """
        This helper function prompts the user to manually enter a Hand list separated by spaces for scoring.
        """

def main():
    this_hand_presently_dealt = Hand()
    for i in range(6):
        this_hand_presently_dealt.hand_of_cards_list = this_hand_presently_dealt.add_card_to_hand()
    this_hand_presently_dealt.score_this_hand()

main()