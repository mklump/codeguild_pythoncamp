# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by Matthew James K
LAB/STEP requirements:
The city of Portland has rain gauges that keep track of rainfall.
[A website](http://or.water.usgs.gov/non-usgs/bes/) has text data tables the history of all the daily measurements at these gauges.

Python gives you a module called `urllib.request` you can use a function `urllib.request.urlopen(url)` which returns a file-like object.
Look at [the docs](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for that module.

One little difference is the file-like object doesn't return strings, it returns **bytes**.
Use the following code snippet to make it return strings.
```python
import urllib.request

with urllib.request.urlopen('http://www.gutenberg.org/ebooks/1342.txt.utf-8') as pride_and_prejudice_file:
  lines = [byte_line.decode('utf-8') for byte_line in pride_and_prejudice_file]
```

Use that module to read [the history of the gauge at Sunnyside School](http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain). It looks like:
URL replaced with David's github.com account: https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain
```
TEXT HEADER...

            Daily  Hourly data -->
   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
MORE...
```
The amounts are in hundredths of inches.

* Parse and store the **daily total** data for each day.
* Find and print out the specific date with the most rain.
* Find and print out the year with the most rain.

## Advanced
* Find and print the day of the year with the most rain on average.
E.g. December 30th has 1" of rain on average.
* Allow someone to type in a date in the future and, using the average value predict the amount of rain.
"""
import urllib.request
import re
#import operator
#import os

"BE IT KNOWN ANYONE WHO DARES TO JUDGE THIS CODE -- I WILL NOT BE JUDGED BY YOU OR BY ANYONE -- THERE IS ONLY ONE WHO WILL JUDGE ME. Now off with the likes of you!"

def show_program_intro():
	"""
	Prints to console standard out an introduction for this program
	"""
	print('This program reads a URL for byte stream data, and performs calculations on it.')
	print('Press enter to continue...')
	input()

def read_rain_gauge_sunnyside_school():
	"""
	This help function opens a byte stream against the requested hard code URL, and retrieves the byte stream from URL request.
	:returns: the Sunny Side School rain totals as requested utf-8 text lines in hundredths of inches per day/hour
	"""
	with urllib.request.urlopen('https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain') as sunnyside_rain:
		raw_unparsed_byte_stream_url_source = [byte_line.decode('utf-8') for byte_line in sunnyside_rain]
	# end with block/close byte stream
	return raw_unparsed_byte_stream_url_source

def print_rain_guage_output(rain_data_from_stream_datasource):
	"""
	This helper function is a simple test to print out the unformated/unparsed data from the utf-8 byte stream.
	:param 1: the raw rain data to print out
	"""
	for row in rain_data_from_stream_datasource:
		print('{}'.format(row))

def parse_regex_daily_total(raw_rain_data_unparsed_dates_and_daily_totals):
	"""
	This helper function accepts the raw rain total data from the URL, and uses a regular expression to parse the totals.
	:param 1: raw rain total data from URL data source
	:returns: the data for the rain totals as a dictionary with key as the date, and value as the rain total for that day
	"""
	parsed_date_and_rain_totals_dict = {}
	re_matched_strings_output_2_groups = ''
	for row in raw_rain_data_unparsed_dates_and_daily_totals:
		re_matched_strings_output_2_groups = re.search('([0-9]*-[A-Z]*-[0-9]*)[ ]*([0-9]*)', row) # match exactly two string groups and return them, the left group is the dates and right group is the daily totals
		if None == re_matched_strings_output_2_groups:
			continue
		if False == re_matched_strings_output_2_groups.string.strip().split()[0][0].isdigit(): # matched sting is still not yet starting row, has '------' etc.
			continue
		parsed_date_and_rain_totals_dict[re_matched_strings_output_2_groups.group(1)] = re_matched_strings_output_2_groups.group(2) # keeps types consistanct instead of int() cast, data type first as str()
	return parsed_date_and_rain_totals_dict

def sort_rain_dictionary(raindata_dict_from_urlstream):
	"""
	The helper function accepts a dictionary for the rain, then sorts the data by date in desending order as the return value.
	:param 1: raindata_dict_from_urlstream is the rain data dictionary to sort
	:returns: the sorted dictionary as a list return value without loss of data
	"""
	raindata_from_dictionary_to_sort = raindata_dict_from_urlstream.items() #[ [key, value] for key, value in raindata_dict.items() ] # .items() already gives the unpacking of the dictionary items
	sorted_dictionary_raindata = sorted(raindata_from_dictionary_to_sort, reverse=True) # Sort accept a second arguement kyword reverse=True Do not leave space on KEY assignment here only
	return sorted_dictionary_raindata

def get_day_highest_rainfall(raindata_list_raw_values_from_urlstream):
	"""
	This helper function finds the largest daily rainfall total for a single day.
	:param 1: the SORTED raindata_list as the rain fall totals per day as a list
	:returns: the largest rain fall recorded for all recorded days as a list
	"""
	list_with_nonempty_values = remove_emptystring_values(raindata_list_raw_values_from_urlstream) # casting the comparison key to another type to compare is undesirable, first cast the type to the correct data type, then store it in the list for comparison.
	highest_day_rain = max(list_with_nonempty_values, key=lambda row: int(row[1])) # lambda expression works IFF there is NO empty string bad data before cast to int! '' Empty string data in second element column must first be removed from source.
	return highest_day_rain

def remove_emptystring_values(raindata_list_raw_values_from_urlstream):
	"""
	The incomming data source for the rain totals at the URL has '' Empty string for totals bad data!
	We are the ones that must deal with this. This helper fuction accepts the raw list source, and removes
	the '' empty string rain totals read in from the source.
	:param 1: raindata_list raw rain totals data as list
	:returns: same raindata_list raw data with '' rain total values REMOVED
	"""
	for row in raindata_list_raw_values_from_urlstream: # Use ONLY THIS LOOP FORM or while loop similar form to remove bad data from list of lists!!!
		if '' == row[1]:
			raindata_list_raw_values_from_urlstream.remove(row)
	raindata_list_with_bad_data_removed = raindata_list_raw_values_from_urlstream
	return raindata_list_with_bad_data_removed # [ raindata_list.remove(row) for row in raindata_list if '' == row[1] ] # list conprehention will NEVER work for removing bad data from a list of lists, use only the prior form!

def print_highest_rainfall(properly_organized_date_and_totals):
	"""
	This helper function prints out the highest rainfall from the specified found value.
	:param 1: rainfall as the highest rain fall value found from the data stream
	"""
	print('The highest rain fall value found was: {} on {}.'.format(properly_organized_date_and_totals[1], properly_organized_date_and_totals[0]))

def get_year_with_most_rain(totals_list_per_day_from_datasource):
	"""
	This helper function accepts the total amount of rain fall list per day in hundreths of inches,
	calcuates the highest rainfall for all the recorded and retrieved data and returns that value.
	:param 1: totals_list_per_day_from_datasource as all retrieved and calcuable rainfall data
	:returns: the year with the most rain as dictionary single entry search by value
	"""
	rain_by_year_collection = {}
	for row in totals_list_per_day_from_datasource:
		year_component_of_parsed_date = row[0].split('-')[2]
		if None == rain_by_year_collection.get(year_component_of_parsed_date):
			rain_by_year_collection[year_component_of_parsed_date] = 0
		if '' == row[1]:
			continue
		rain_by_year_collection[year_component_of_parsed_date] += int(row[1])
	max_rainy_year = max(rain_by_year_collection.items(), key=max_rain_compare) # use .items() and always searches based on the structure given, here .items() returns the dictionary as a tuple only.
	year_with_most_rain = { max_rainy_year[0] : max_rainy_year[1] }
	#year_most_rain = { key : value for key, value in rain_by_year.items() if value == max_value[1] } # find key/year in the dictionary by value/rain reverse thinking.
	return year_with_most_rain

def max_rain_compare(rain_by_year):
	"""
	This helper function accepts the rain_by_year.items() key, value as a list of two tuples, and returns
	second element to sort by.
	:param 1: rain_by_year.items() key, value as a list of two tuples
	:returns: the second element of the items() two tuples collection to sort by
	"""
	return rain_by_year[1]

def print_year_most_rain(year_highest_rain_daily_total):
	"""
	Accepts the calculated year with the most rain as a dictionary and prints it to console standard out.
	:param 1: year_highest_rain_daily_total is the year with the highest rain as incomming dictionary
	"""
	# [ [key, value] for key, value in year_highest_rain_daily_total.items() ]
	list_print_out = list(year_highest_rain_daily_total.items()) # cast the dictionary for output as properly taught be calling the .items() method of the dictionary type
	print('The year with the highest rain amount was: {} with rain amount {}.'.format(list_print_out[0][0], list_print_out[0][1]))

	"BE IT KNOWN ANYONE WHO DARES TO JUDGE THIS CODE -- I WILL NOT BE JUDGED BY YOU OR BY ANYONE -- THERE IS ONLY ONE WHO WILL JUDGE ME. Now off with the likes of you!"

def main():
	"""
	Main function/test driver main single thread of execution for this console program. The call stack is in the order in which the functions appear.
	"""
	show_program_intro()
	byte_lines = read_rain_gauge_sunnyside_school()
	#print_rain_guage_output(byte_lines)
	totals_dict = parse_regex_daily_total(byte_lines)
	totals_list = sort_rain_dictionary(totals_dict)
	highest_rainfall = get_day_highest_rainfall(totals_list)
	print_highest_rainfall(highest_rainfall)
	year_highest_rain = get_year_with_most_rain(totals_list)
	print_year_most_rain(year_highest_rain)

main()