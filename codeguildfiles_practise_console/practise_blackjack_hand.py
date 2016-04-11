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

class Card(object): # In Python as in all other higher languages, a class is only a container for data and for structuring it.
    """
    This class Card represents a single physical item from a 52 card deck used in a poker game.
    """
    def __init__(self, card_type_of_thirteen, suite): # A card does not intrinsicly know a point_value attribute until it is scored
        """
        Three argument "magic" constructor/object initializer for SPACE on the PYTHON MANAGED HEAP
        """
        self.card_type_of_thirteen = card_type_of_thirteen
        self.suite = suite

    def __repr__(self):
        """
        String definition representation of this object. 'this' instead of 'self' but are still the same.
        Prints out the point_value for this particular card.
        """
        return 'This Card card_type_of_thirteen is \'{0}\', and the suite is \'{1}\''.format(self.card_type_of_thirteen, self.suite)

    def __eq__(self, other_card):
        """
        Overloaded == equality operator
        """
        return self.card_type_of_thirteen == other_card.card_type_of_thirteen and self.suite == other_card.suite
# end class Card:

class Hand(object):
    """
    This class Hand represents a specific Blackjack collection of Cards for use in a Blackjack game round.
    """
    def __init__(self, hand_of_cards_list=[]):
        """
        Two argument "magic" constructor/object initializer for SPACE on the PYTHON MANAGED HEAP
        :param 1: hand_of_cards_list as the list of working Card objects in this/self Hand object
        """
        self.hand_of_cards_list = hand_of_cards_list # Correct only build the hand_of_cards_list as the only attribute

    def __repr__(self):
        """
        String definition representation of this object. 'this' instead of 'self' but are still the same.
        The repr magic function prints out the list of cards in this hand.
        """
        return 'Hand({0})'.format(self.hand_of_cards_list) # Correct on printing the only attribute, formatting the list output can be improved

    def __eq__(self, other_hand):
        """
        Overloaded == equality operator
        """
        for card in range(len(self.hand_of_cards_list)): # Comparison using == of two list accomplished the same here on __eq__
            if self.hand_of_cards_list[card] != other_hand.hand_of_cards_list[card]:
                return False
        #end for checking
        return True

    def add_random_card_to_hand(self):
        """
        This class function adds a single random Card object to the list(Card) collection and returns the modified list.
        :returns: The modified input list with the new added card just now drawn
        """
        #card_value_type = namedtuple('card_value_type', ('2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace'))
        #accessible through the dot operator such as card_value_type.2 or card_value_type.Jack or card_value_type.Ace

        rand_pokercard_type = random.randint(1, 13)
        get_next_card_to_draw().point_value = self.get_card_point_value(rand_pokercard_type, '', next_card_to_draw)
        self.hand_of_cards_list.append(next_card_to_draw)
        return self.hand_of_cards_list

    @staticmethod
    def get_next_card_to_draw():
        """
        The class function retrieves the next Card() instance that is being processed before it is added to
        the list of cards in this Hand().
        :returns: the next_card_to_draw instance that was instantiated if it must be before it is added
        """
        if None == next_card_to_draw:
            next_card_to_draw = Card(str(), 0, str())
        return next_card_to_draw

    def get_card_point_value(self, rand_pokercard_type, card_by_specific_name, next_card_to_draw): # TODO: Refactor, move next_card_to_draw to get_next_card_to_draw()
        """
        This class fuction accepts a specific card based on the the integer representation of each
        '2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING, ACE' card names.
        and returns the associated poker point value of that specific card.
        :param 1: rand_pokercard_type is the number as an integer of next Card object to create to add to the Hand
        :param 2: card_by_specific_name as the user defined specific card to get the point value of as a string
        :param 3: next_card_to_draw as the next selected Card object being worked with to add to the self.hand_of_cards_list
        :returns: associated poker point value of that specific card
        """
        card_type_lookup = {      # Do not define if-else-elif value constant lookups in Python
            1 : ['2', 2],         # Instead the Python dictionary replaced switch() in C# and C++ for
            2 : ['3', 3],         # constant lookups.
            3 : ['4', 4],
            4 : ['5', 5],
            5 : ['6', 6],
            6 : ['7', 7],
            7 : ['8', 8],
            8 : ['9', 9],
            9 : ['10', 10],
            10 : ['JACK', 10],
            11 : ['QUEEN', 10],
            12 : ['KING', 10],
            13 : ['ACE', 11], # mutilline constant structures only allow unused final comma at the end of declaration
            }
        next_card_drawn = next_card_to_draw
        for card_type in card_type_lookup:
            if rand_pokercard_type == card_type or rand_pokercard_type == card_type_lookup[card_type][0]: #TODO: String look error on add specific card
                next_card_drawn.card_type_of_thirteen = card_type_lookup[card_type][0]
                next_card_drawn.point_value = card_type_lookup[card_type][1]
                next_card_drawn.suite = None
        return next_card_drawn.point_value

    def add_specific_card_to_hand(self, specific_card_without_suite):
        """
        This class function adds a single specific Card object to the list(Card) collection and returns the modified list.
        :param 1: specific_card_without_suite is the next specific user defined Card object to create to add to the Hand as a string
        :returns: The modified input list with the new added card just now drawn
        """
        next_card_to_draw = Card(str(), 0, str())
        self.get_card_point_value(specific_card_without_suite, None, next_card_to_draw)
        self.hand_of_cards_list.append(next_card_to_draw)
        return self.hand_of_cards_list

    def score_this_hand(self, hand_of_cards_list=[]):
        """
        This class function accepts the List() [] of Card objects of this self.hand_of_cards_list,
        and scores this particular Hand based on the card values drawn Card.point_value.
        :param 1: hand_of_cards_list as the card list of Hand instance member of all presently drawn cards in this hand
        :returns: The total score based on black jack rules for this Hand
        """
        current_points = 0
        for card in self.hand_of_cards_list:
            current_points += card.point_value
            is_score_over = self.is_score_over_twentyone(current_points)
            current_points = is_score_over[1]
            if True == is_score_over[0]:
                print_score_busted(current_points)
                break
        return current_points

    def is_score_over_twentyone(self, current_points): #Python claims pass by OBJECT VALUE.
        """
        This class function tests whether or not the current total score of this Hand is over 21, if it is then this
        fuction returns True, otherwise False.
        :param 1: current_points as the current running total of card value not yet over 21
        :returns: List of True if the score of this Hand.hand_of_cards_list is over 21, other wise False for the first
        return value in the list, and also the current_points modified point total without the loss of either state value
        """
        return_value = [] # This is a test in Pyton on the affectiveness of returning more that one value [a boolean, and an integer]
        for card in self.hand_of_cards_list:
            current_points = self.modify_points_on_ace_and_over_twentyone(card, current_points)
        return_value.append(current_points > 21)
        return_value.append(current_points)
        return return_value

    def modify_points_on_ace_and_over_twentyone(self, card_in_hand, current_points):
        """
        This class function modifies the current_points of this hand by -10 points if the current card being tested
        is an ACE and the score has busted over 21, thus making the ACE's point value 1 instead of 11.
        :param 1: card_in_hand as the current card in the hand being tested as type Card
        :param 2: current_points as the current score of this hand to be modified per the black jack rules
        """
        if 'ACE' == card_in_hand.card_type_of_thirteen and current_points > 21:
            current_points -= 10
        return current_points
# end class Hand:

def prompt_the_user_to_input_a_hand():
    """
    This helper function prompts the user to manually enter a Hand list separated by spaces for scoring.
    :returns: The Hand of n number randomly selected cards to make up the Hand as list of Card
    """
    print('Please input an n number randomly selected cards separated by spaces:')
    print('--> Example: 2 3 4 5 6 7 8 9 10 JACK QUEEN KING ACE <--')
    return input().split(' ')

def test_drawing_a_hand_of_n_random_cards(number_cards_to_randomly_draw=0):
    """
    This helper function could be considered a Unit Test for a drawing a Hand of 3 Card objects
    for use in the main() harness, and returns nothing.
    :param 1: number_cards_to_randomly_draw as the number of randomly generated Cards must be an integer
    """
    test_hand_of_cards = Hand()
    test_hand_of_cards.hand_of_cards_list.clear()
    for i in range(int(number_cards_to_randomly_draw)): # Testing drawing a hand of three cards
        test_hand_of_cards.hand_of_cards_list = test_hand_of_cards.add_random_card_to_hand()
    score_of_this_hand = test_hand_of_cards.score_this_hand()
    print_score_calculated(score_of_this_hand)

def test_drawing_exact_user_defined_hand(user_defined_hand_of_cards):
    """
    This helper function accept a list of strings that represent Card objects to be created
    from the user, and returns the list of Card objects as the Hand.
    :param 1: user_defined_hand_of_cards as the list of strings that represent card to be instantiated.
    :returns: the list of Card objects as the Hand to be printed to standard out.
    """
    test_hand_of_cards = Hand()
    test_hand_of_cards.hand_of_cards_list.clear()
    for card_name in user_defined_hand_of_cards:
        test_hand_of_cards.hand_of_cards_list = test_hand_of_cards.add_specific_card_to_hand(card_name)
    score_of_this_hand = test_hand_of_cards.score_this_hand()
    print_score_calculated(score_of_this_hand)

def print_score_busted(actual_score_of_hand):
    """
    This helper function prints to standard out a message when the total score busts the 21 limit.
    :param 1: actual_score_of_hand as the current actual score of this hand as an integer
    """
    print('You busted with your score over 21! Actual score was: {0}'.format(actual_score_of_hand))

def print_score_calculated(score_last_hand_calculated):
    """
    The helper function prints the score of the last Hand of Cards calculated to standard out.
    :param 1: score_last_hand_calculated as the score calculated of that last hand drawn as an integer
    """
    print('The last score calculated of that last Hand of Cards that was drawn was: {0}'.format(score_last_hand_calculated))

def main():
    test_drawing_a_hand_of_n_random_cards(3) # test a Hand of 3 Cards
    test_drawing_a_hand_of_n_random_cards(6) # test a Hand of 6 Cards
    user_defined_hand_of_cards = prompt_the_user_to_input_a_hand() # Testing have the user input a hand of n number randomly selected cards to
                                                                   # make up the Hand.
    test_drawing_exact_user_defined_hand(user_defined_hand_of_cards)

main()