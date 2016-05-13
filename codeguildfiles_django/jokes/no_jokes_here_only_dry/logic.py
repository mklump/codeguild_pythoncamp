# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file no_jokes_here_only_dry/views.py
by Matthew James K on 5/12/2016
"""

jokes = []
"""
This jokes jagged array global variable will have the first item of each inner array as the story
setups, and the second as the punch lines.
"""

def get_all_story_setups():
    """
    This function retrieves all the story setups from the first item of the inner array of the jokes outer array.
    :returns: an array of the story setups from the jokes array
    """
    story_setups = []
    for story in jokes:
        story_setups.append(story[0])
    return story_setups

def get_all_punch_lines():
    """
    This function retrieves all the punch lines from the second item of the inner array of the jokes outer array.
    :returns: an array of the punch lines from the jokes array
    """
    punch_lines = []
    for punched in jokes:
        punch_lines.append(punched[1])
    return punch_lines