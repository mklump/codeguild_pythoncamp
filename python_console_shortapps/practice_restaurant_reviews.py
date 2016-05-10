# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
By Lab Partners: Matthew James K, Peter Dziuba, Matthew Voelpel
Date: 4/4/2016
LAB/STEP requirements:

Practice: Restaurant Reviews
We're going to make a mini version of Yelp. There are local business listings and users can post reviews, with a rating and some text, of each business.

Make a class that represents a review: it will have "rating" and "review text" fields.
Make a class that represents a business: it will have "name" and a list of reviews fields.
Load the following data into those classes. Don't use raw_business_review_data for any further operations.
raw_business_review_data = [
  {
    'business_name': 'Salt & Straw',
    'reviews': [
      {'rating': 5, 'text': 'Lucious ice cream!'},
      {'rating': 4, 'text': 'Super tasty, but such a long line!'}
      {'rating': 2, 'text': 'Overrated, but I like sugar.'}
    ],
  },
  {
    'business_name': 'Voodoo Donuts',
    'reviews': [
      {'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
      {'rating': 5, 'text': 'Pink building is so cute!'}
      {'rating': 2, 'text': 'Diabetes inducing.'}
    ],
  },
]
Add a function to the business class that returns the average rating.
Implement searching by name: Prompt for the a name of a business, and print out the average rating for that business and one review.

Add a user class: it will have a "user name" field.

Add a "user name" field to the review class.
In real life, data like this is not hierarchical. This is so you can ask questions like "what are all the reviews I wrote?" Let's denormalize or break apart the hierarchy we currently have.

Add a "business name" field to the review class.
Remove the list of reviews field from the business class.
Load the following data into those refactored classes. Don't use these variables for any further operations.
raw_business_data = [
  {
    'business_name': 'Salt & Straw',
  },
  {
    'business_name': 'Voodoo Donuts',
  },
]
raw_user_data = [
  {'user_name': 'Abby'},
  {'user_name': 'Helen'},
  {'user_name': 'Bobby'},
]
raw_review_data = [
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 5, 'text': 'Lucious ice cream!'},
  {'user_name': 'Bobby', 'business_name': 'Salt & Straw', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 2, 'text': 'Overrated, but I like sugar.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
]
Re-implement the searching by name above.
Implement searching for reviews by user: Prompt for the a name of a user, and print out all reviews for that user.
"""
import random

class Review:
    def __init__(self, business_name, user_name, rating, review):
        self.rating = rating
        self.business_name = business_name
        self.user_name = user_name
        self.review = review

    def __repr__(self):
        my_str = "{}: {} rating: {}".format(self.business_name,
                                            self.review, self.rating)
        return my_str

class Business:
    def __init__(self, business_name):
        self.business_name = business_name

    def __repr__(self):
        '{}'.format(self.business_name)

class User:
    def __init__(self, user_name):
        self.user_name = user_name

def search_business_name(review_class_list, user_input_string):
    review_list = [i for i in review_class_list
                   if user_input_string in i.business_name]
    average_counter = sum([i.rating for i in review_class_list
                           if user_input_string in i.business_name])
    average_rating = average_counter / len(review_list)
    print(average_rating)
    print(review_list[random.randint(1, (len(review_list) - 1))])

def search_user_name(review_class_list, user_input_string):
    list_of_user_reviews = [i for i in review_class_list
                            if user_input_string in i.user_name]
    print(list_of_user_reviews)

def main():
    business_class_list = [Business(i['business_name']) for i in raw_business_data]
    user_class_list = [User(i['user_name']) for i in raw_user_data]
    review_class_list = [Review(i['business_name'], i['user_name'],
                         i['rating'], i['text']) for i in raw_review_data]
    user_search = input('Enter a business name\n: ')
    search_business_name(review_class_list, user_search)
    user_search_again = input('Enter a user name\n: ')
    search_user_name(review_class_list, user_search_again)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
