# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file jokes/logic.py
by Matthew James K on 5/12/2016
"""
from datetime import datetime
#import json

jokes = []
"""
This jokes jagged array global variable will have the first item of each inner array as the story
setups, and the second as the punch lines.
"""

def save_submitted_joke(setup_story, punch_line):
    """
    This function accepts the setup_story of the dry dock, knee slapper joke, and also the punch_line of the dry
    dock, knee slapper joke, and saves that information as an array of two string to the jokes global array.
    :param 1: setup_story string represents the setup or story that make the punch line more believeable
    :param 2: punch_line string represents the part that is supposed to make you laugh or slap your knee
    """
    jokes.append([setup_story, punch_line, str(datetime.now())])

def get_all_jokes_data():
    """
    This ajax use function retrieves the entire jokes array "backend" both story setups and punch lines.
    """
    return jokes

def ajax_save_submitted_joke(story_setup, punch_line):
    """
    This ajax use function saved the sent story_setup, and the punch_line from the ajax form save to the
    global list 'backend' data structure here.
    """
    return save_submitted_joke(story_setup, punch_line)

#def get_json_repr_of_jokes():
#    """
#    This function returns back the json serialized representation of the jokes global array.
#    :returns: jokes array as a json serialized string
#    """
#    serialized_string = json.dumps(jokes) # Serialize this array into a string to be stored into a hidden html control.
#    return serialized_string;

#def get_all_story_setups():
#    """
#    This function retrieves all the story setups from the first item of the inner array of the jokes outer array.
#    :returns: an array of the story setups from the jokes array
#    """
#    story_setups = []
#    for story in jokes:
#        story_setups.append(story[0])
#    return story_setups