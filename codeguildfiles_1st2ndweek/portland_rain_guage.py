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
	with urllib.request.urlopen('http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain') as sunnyside_rain:
		byte_lines = [byte_line.decode('utf-8') for byte_line in sunnyside_rain]
	# end with block/close byte stream
	return byte_lines

def print_rain_guage_output(rain_data):
	"""
	This helper function is a simple test to print out the unformated/unparsed data from the utf-8 byte stream.
	:param 1: the raw rain data to print out
	"""
	for row in rain_data:
		print('{}'.format(row))

def parse_regex_daily_total(rain_total):
	"""
	This helper function accepts the raw rain total data from the URL, and uses a regular expression to parse the totals.
	:param 1: raw rain total data from URL
	:returns: the data for the rain totals as a dictionary with key as the date, and value as the rain total for that day
	"""
	dailytotal_list = {}
	match = ''
	for row in rain_total:
		match = re.search('([0-9]*-[A-Z]*-[0-9]*)[ ]*([0-9]*)', row) # match exactly two string groups and return them
		if None == match:
			continue
		if False == match.string.strip().split()[0][0].isdigit():
			continue
		dailytotal_list[match.group(1)] = match.group(2)
	return dailytotal_list

def sort_rain_dictionary(raindata_dict):
	"""
	The helper function accepts a dictionary for the rain, then sorts the data by date in desending order as the return value.
	:param 1: raindata_dict is the rain data dictionary to sort
	:returns: the sorted dictionary as a list return value without loss of data
	"""
	data = [ [key, value] for key, value in raindata_dict.items() ]
	data = sorted(data) # Do not leave space on KEY assignment here only
	data.reverse()
	retval = data # { key : value for key, value in data } # may need later for list comprehention cast back to dictionary
	return retval

def get_day_highest_rainfall(raindata_list):
	"""
	This helper function finds the largest daily rainfall total for a single day.
	:param 1: the SORTED raindata_list as the rain fall totals per day as a list
	:returns: the largest rain fall recorded for any particular day as a list
	"""
	retval = []
	rain = 0
	for row in raindata_list:
		if '' == row[1]:
			continue
		if int(rain) < int(row[1]):
			retval = row
			rain = row[1]
	return retval

def print_highest_rainfall(rainfall):
	"""
	This helper function prints out the highest rainfall from the specified found value.
	:param 1: rainfall as the highest rain fall value found from the data stream
	"""
	print('The highest rain fall value found was: {} on {}'.format(rainfall[1], rainfall[0]))

# begin program main/test
show_program_intro()
byte_lines = read_rain_gauge_sunnyside_school()
#print_rain_guage_output(byte_lines)
totals_dict = parse_regex_daily_total(byte_lines)
totals_list = sort_rain_dictionary(totals_dict)
highest_rainfall = get_day_highest_rainfall(totals_list)
print_highest_rainfall(highest_rainfall)
# end program main/test