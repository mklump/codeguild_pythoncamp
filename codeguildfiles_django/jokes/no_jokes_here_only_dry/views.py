# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file no_jokes_here_only_dry/views.py
by Matthew James K on 5/12/2016
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

from no_jokes_here_only_dry import logic

def render_index(request):
    """
    This function renders the presentation of jokes for index.html main page.
    That page also containts the submission form for jokes.
    """
    assert isinstance(request, HttpRequest)
    story_setups = logic.get_all_story_setups()
    serialized_string = logic.get_json_repr_of_jokes()
    return render(
        request, # use this request object for this rendering
        'no_jokes_here_only_dry/index.html', # navigate to this page for this request handling
        context_instance = RequestContext(request, # use THIS context_instance for these context variables for the index.html template
        {
            'story_setups':story_setups,
            'serialized_string':serialized_string,
            'title':'Not quite so - Jokes Form',
            'time':str(datetime.now()),
        })
    )

def submit_dry_dock_joke(request):
    """
    This function accepts the form post parameters from the index.html form control,
    and updates the storage place currently as the global variable logic.jokes list.
    """
    assert isinstance(request, HttpRequest)
    setup_story = request.POST['setup_story']
    punch_line = request.POST['punch_line']
    logic.save_submitted_joke(setup_story, punch_line)
    return render_index(request) # Do not call render() here as response unless calling HttpResponse('') without request, template_name, and context!