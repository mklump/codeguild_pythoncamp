# -*- coding: utf-8 -*-
"""
Created on Sun 2016-01-24T07:54:10.625084

@author: Kirby Urner

Intro to classes (2 of 2)

Demonstrates:
* Python's unicode capabilities
* The 'placeholder' nature of self (and cls):  not keyword(s)
* Decorator syntax replacing toggle = classmethod(toggle)

自我 (zì wǒ) is a placeholder for self (i.e. instance identity)
"""

from random import choice

class Earth_creature:
    pass

class Smell:
    pass  # I will add more code here

class Mammal:
    
    def __init__(自我):
        自我.stomach = [ ]  # I'm hungry
        
    def eat(自我, еда):
        自我.stomach.append(еда)  # еда = food
        
class Dog(Mammal):
    
    dangerous = True
    
    def toggle(cls):
        if cls.dangerous:
            cls.dangerous = False
        else:
            cls.dangerous = True
    
    def __init__(自我, name, breed):
        super().__init__()
        自我.name = name
        自我.breed = breed
        
    def bark(自我, how_many):  # expect int
        return "Bark! " * how_many
        
    def __add__(自我, other):
        return 自我.name + " " + other.name
    
    def __call__(自我, food):
        自我.eat(food)

    def __repr__(自我):
        return "Dog('{}', '{}')".format(自我.name, 自我.breed)
            
    def sniff(自我, the_smell):
        if the_smell.food_smell:
            return "Whine!"
    
class Die:  # as in dice
    """model a die of n sides"""
    
    def __init__(自我, sides = None):
        if not sides:
            自我.sides = list(map(str, range(1,7)))
        else:
            自我.sides = sides
        自我.current_value = 自我.sides[0]
        
    def roll(自我):
        """pick a side, any side..."""
        自我.current_value = choice(自我.sides)
        return 自我.current_value
        
    def __repr__(自我):
        return "Die with value {}".format(自我.current_value)

if __name__ == "__main__":    
    
    # Dog section
    puppy = Dog("Snoopy", "Beagle")
    print(puppy.bark(3))
    puppy.eat("steak!")
    print("Inside puppy:", puppy.stomach)
    yummy = Smell()
    yummy.food_smell = True
    print(puppy.sniff(yummy))
    
    # Die section
    it, it1, it2, it3 = Die(), Die(), Die(), Die()
    print((it2.roll(), it3.roll()))
    print(it.roll())
    print(it.roll())
    print(it.roll())
    print(it.roll())
    print(it)
    print("it:", it.__dict__)
    print("it2:", it2.__dict__)

