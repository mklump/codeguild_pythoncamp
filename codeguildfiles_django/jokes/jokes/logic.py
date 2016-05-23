# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file jokes/logic.py
by Matthew James K on 5/12/2016
"""
from datetime import datetime

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

def get_story_setups_data():
    """
    This function retrieves the story setup part of the jokes global array data.
    :returns: an array [] of the story setup part of the jokes global array data with the associated time stamp
    """
    story_setups = ''
    for joke in jokes:
        story_setups += joke[0] + ' ' + joke[2]
    return story_setups

def get_punch_lines_data():
    """
    This function retrieves the punch line part of the jokes global array data.
    :returns: an array [] of the punch line part of the jokes global array data with the associated time stamp
    """
    punch_lines = ''
    for joke in jokes:
        punch_lines += joke[1] + ' ' + joke[2]
    return punch_lines

def ajax_save_submitted_joke(story_setup, punch_line):
    """
    This ajax use function saved the sent story_setup, and the punch_line from the ajax form save to the
    global list 'backend' data structure here.
    """
    return save_submitted_joke(story_setup, punch_line)