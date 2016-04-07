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
        Three argument "magic" constructor/object initializer for SPACE on the PYTHON MANAGED HEAP
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
        Two argument "magic" constructor/object initializer for SPACE on the PYTHON MANAGED HEAP
        :param 1: hand_of_cards_list as the list of working Card objects in this/self Hand object
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

    def add_random_card_to_hand(self):
        """
        This class function adds a single random Card object to the list(Card) collection and returns the modified list.
        :returns: The modified input list with the new added card just now drawn
        """
        #card_value_type = namedtuple('card_value_type', ('2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace'))
        #accessible through the dot operator such as card_value_type.2 or card_value_type.Jack or card_value_type.Ace

        next_card_to_draw = Card(str(), 0, str())
        rand_pokercard_type = random.randint(1, 13)
        next_card_to_draw.point_value = self.get_card_point_value(rand_pokercard_type, '', next_card_to_draw)
        self.hand_of_cards_list.append(next_card_to_draw)
        return self.hand_of_cards_list

    def get_card_point_value(self, rand_pokercard_type, card_by_specific_name, next_card_to_draw):
        """
        This class fuction accepts a specific card based on the the integer representation of each
        '2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING, ACE' card names.
        and returns the associated poker point value of that specific card.
        :param 1: rand_pokercard_type is the number as an integer of next Card object to create to add to the Hand
        :param 2: card_by_specific_name as the user defined specific card to get the point value of as a string
        :param 3: next_card_to_draw as the next selected Card object being worked with to add to the self.hand_of_cards_list
        :returns: associated poker point value of that specific card
        """
        card_type_lookup = { # TODO: Do not define if-else-elif value constant lookups in Python
            1 : ['2', 2],         # Instead the Python dictionary replaced switch() in C# and C++ for constant lookups.
            2 : ['3', 3],
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
            if rand_pokercard_type == card_type: #TODO: String look error on add specific card
                next_card_drawn.suite = None
                next_card_drawn.card_type_of_thirteen = card_type_lookup[card_type][0]
                next_card_drawn.point_value = card_type_lookup[card_type][1]
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
                self.print_score_busted(current_points)
                break                
        return current_points

    def is_score_over_twentyone(self, current_total_points):
        """
        This class function tests whether or not the current total score of this Hand is over 21, if it is then this
        fuction returns True, otherwise False.
        :returns: True if the score of this Hand.hand_of_cards_list is over 21, other wise False
        """
        for card in self.hand_of_cards_list:
            if 11 == card.card_type_of_thirteen and current_total_points > 21:
                current_total_points -= 10
        return current_total_points > 21

    def print_score_busted(self, actual_score_of_hand):
        """
        This class function prints to standard out a message when the total score busts the 21 limit.
        :param 1: actual_score_of_hand as the current actual score of this hand as an integer
        """
        print('You busted with your score over 21! Actual score was: {0}'.format(actual_score_of_hand))

    def print_score_calculated(self, score_last_hand_calculated):
        """
        The class function prints the score of the last Hand of Cards calculated to standard out.
        :param 1: score_last_hand_calculated as the score calculated of that last hand drawn as an integer
        """
        print('The last score calculated of that last Hand of Cards that was drawn was: {0}'.format(score_last_hand_calculated))
# end class Hand:

def prompt_the_user_to_input_a_hand():
    """
    This helper function prompts the user to manually enter a Hand list separated by spaces for scoring.
    :returns: The Hand of n number randomly selected cards to make up the Hand as list of Card
    """
    print('Please input an n number randomly selected cards separated by spaces:')
    print('--> Example: 2 3 4 5 6 7 8 9 10 JACK QUEEN KING ACE <--')
    return input().split(' ')

def test_drawing_a_hand_of_n_random_cards(number_cards_to_randomly_draw = 0):
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
    test_hand_of_cards.print_score_calculated(score_of_this_hand)

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
    test_hand_of_cards.print_score_calculated(score_of_this_hand)

def main():
    test_drawing_a_hand_of_n_random_cards(3) # test a Hand of 3 Cards
    test_drawing_a_hand_of_n_random_cards(6) # test a Hand of 6 Cards
    user_defined_hand_of_cards = prompt_the_user_to_input_a_hand() # Testing have the user input a hand of n number randomly selected cards to make up the Hand.
    test_drawing_exact_user_defined_hand(user_defined_hand_of_cards)

main()