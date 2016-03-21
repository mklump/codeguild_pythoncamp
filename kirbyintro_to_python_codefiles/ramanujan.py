# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:40:46 2015

See:  https://crypto.stanford.edu/pbc/notes/pi/ramanujan.html

@author: kurner

LAB:

Write a unittest to confirm convergence to:

'3.141592653589793238462643383279502884197169
39937510582097494459230781640628620899862803
48253421170'

after n steps.
"""

import unittest

from decimal import *
# getcontext().prec = 100  # setting high precision standard!
from math import factorial as fact

import unittest

def pieinsky():
    c1 = Decimal(4)
    c2 = Decimal(1103)
    c3 = Decimal(26390)
    c4 = Decimal(396)
    c5 = Decimal(9801)
    # code formatted for readability (make it be one line)
    root8 = Decimal('2.82842712474619009760337744841939615'
                     '7139343750753896146353359475981464956'
                     '9242140777007750686552831454700276')
    i = Decimal(0)
    thesum = Decimal(0)
    while True:
    	term = (fact(c1*i)*(c2 + c3*i))/(pow(fact(i),4)*pow(c4,4*i))
    	thesum = thesum + term
    	yield 1/((root8/c5)*thesum)
    	i += 1


class TestPi(unittest.TestCase):

    def test_outcome(self):
        expected = ('3.141592653589793238462643383'
        '2795028841971693993751058209749445923078'
        '164062862089986280348253421170')
        with localcontext() as c:
            c.prec = 100
            the_gen = pieinsky()
            for _ in range(20):
                next(the_gen)

        self.assertEqual(str(next(the_gen))[:len(expected)], expected)

if __name__ == "__main__":
    unittest.main()
    