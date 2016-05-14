"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file polls/logic.py
by Andrew, Justin, and Matthew James K on 5/13/2016
"""

flavor_to_count = {
    'chocolate': 0,
    'vanilla': 0,
    'strawberry': 0,
}

def add_flavor(vote):
    if vote in flavor_to_count:
        flavor_to_count[vote] += 1

def convert_count_to_percentage(flavor_to_count):
    flavor_to_percentage = {}
    total = return_total(flavor_to_count)
    for vote in flavor_to_count.keys():
        flavor_to_percentage[vote] = (flavor_to_count[vote] / total) * 100
    return flavor_to_percentage

def return_total(flavor_to_count):
    return sum(flavor_to_count.values())

def main():
    flavor_to_percentage = convert_count_to_percentage(flavor_to_count, total)
    return flavor_to_percentage