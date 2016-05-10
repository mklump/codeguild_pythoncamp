# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by Matthew James K
LAB/STEP requirements:

# Practice: Road Trip
In a faraway land, nearby cities are connected by roads.
We've mapped what cities are directly connected by roads and stored them in a dict:
```python
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
```
Traveling from one city to an adjacent one is called a **hop**.

For this sort of problem, you'll want to iteratively visit cities you know you can access while updating:
1. Cities you can access.
1. Cities you've been to.
 

* Let the user enter a city.
Print out all the cities connected to that city.
* Let the user enter a city.
Print out all cities that could be reached through two hops.

Advanced
	• Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.
	• We've also mapped the travel time of each hop:
city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}
When the user enters a city and a number of hops, print out the shortest travel times to each city. Paths with fewer hops
are not necessarily those with the shorter travel times.
"""
def show_program_intro():
	"""
	Prints to console standard out an introduction for this program
	"""
	print('This program performs practise loop logic on a travels dictionary problem.')
	print('Press enter to continue...')
	input()

def get_user_input_city():
	"""
	This helper function prompts the user for the name of a city starting point.
	:returns: The city name starting point as a 
	"""
	print('Please enter a city starting point to find where to travel to:')
	return input()

def get_all_cities_connected(start_city, city_to_accessible_cities):
	"""
	This helper function accepts a city starting point, and retrieves all the cities connected to that city.
	:param 1: start_city as the starting point city to travel from as a string
	:param 2: city_to_accessible_cities as the cities you can reach from your starting point
	:returns: the cities you can travel to as a list
	"""
	retval = []
	for city in city_to_accessible_cities:
		if start_city.lower() == city.lower():
			retval = list(city_to_accessible_cities[city])
			break;
	return retval

def print_all_cities_connected(start_city, cities_connected_list):
	"""
	This helper function prints all the cities connected to the previous specified city of the
	cities_connected_list list.
	:param 1: start_city as the starting point city to travel from as a string
	:param 2: cities_connected_list as the list of connected cities to start_city as a list
	"""
	cities_connected = []
	for city in cities_connected_list:
		cities_connected.append(city + ', ')
	print('The cities connected to {} are: {}'.format(start_city, ''.join(cities_connected).strip(' ').rstrip(',')))

def get_all_two_hop_cities(start_city, city_to_accessible_cities):
	"""
	Traveling from one city to an adjacent one is called a **hop**.
	This helper function retrieves all cities that could be reached through two hops from one starting point city.
	:param 1: start_city as the starting point city to travel from as a string
	:param 2: city_to_accessible_cities as the cities you can reach from your starting point
	:returns: the cities you can travel to using two **hop**'s as a list
	"""
	two_hop_cities = []
	hop_set1 = [] # first hop to city set as list
	hop_set2 = [] # second hop to city set as list
	for city_hop0 in city_to_accessible_cities:
		if start_city.lower() == city_hop0.lower():
			[ two_hop_cities.append(city) for city in city_to_accessible_cities[city_hop0] ]
			hop_set1 = city_to_accessible_cities[city_hop0]
			for city_hop1 in hop_set1:
				for citykey in city_to_accessible_cities:
					if citykey.lower() == city_hop1.lower():
						[ two_hop_cities.append(city) for city in city_to_accessible_cities[city_hop1] ]
						hop_set2 = city_to_accessible_cities[city_hop1]
						for city_hop2 in hop_set2:
							for citykey in city_to_accessible_cities:
								if citykey.lower() == city_hop2.lower():
									[ two_hop_cities.append(city) for city in city_to_accessible_cities[city_hop2] ]
									break
	two_hop_cities = list(set(two_hop_cities)) # remove all the duplicate element entries of the original list in one line by first casting to a set().
	return two_hop_cities

def print_cities_reached_in_two_hops(start_city, two_hop_cities):
	"""
	This helper function prints to standard out all the cities that can be reached by using two hops
	from the specified starting city.
	:param 1: start_city as the starting point city to travel from as a string
	:param 2: two_hop_cities is the cities that can be reached in two hops as a list
	"""
	cities_connected = []
	for city in two_hop_cities:
		cities_connected.append(city + ', ')
	print('The cities that can be reached in two hops starting at {} are: {}.'.format(start_city, ''.join(cities_connected).strip(' ').rstrip(',')))

def main():
    city_to_accessible_cities = {
      'Boston': {'New York', 'Albany', 'Portland'},
      'New York': {'Boston', 'Albany', 'Philadelphia'},
      'Albany': {'Boston', 'New York', 'Portland'},
      'Portland': {'Boston', 'Albany'},
      'Philadelphia': {'New York'}, # ONLY use the added line comma at the end of these multi-line defined data structure literals
    }

    show_program_intro()
    city = get_user_input_city()
    cities_connected = get_all_cities_connected(city, city_to_accessible_cities)
    print_all_cities_connected(city, cities_connected)
    city = get_user_input_city()
    two_hop_cities = get_all_two_hop_cities(city, city_to_accessible_cities)
    print_cities_reached_in_two_hops(city, two_hop_cities)

if __name__ == "__main__":
    sys.exit(int(main() or 0))