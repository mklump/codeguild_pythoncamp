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
    assert isinstance(request, HttpRequest)
    story_setups = logic.get_all_story_setups()
    punch_lines = logic.get_all_punch_lines()
    return render(
        request, # use this request object for this rendering
        'no_jokes_here_only_dry/index.html', # navigate to this page for this request handling
        context_instance = RequestContext(request, # use THIS context_instance for these context variables for the index.html template
        {
            'setups':story_setups,
            'punch_lines':punch_lines,
            'title':'Not quite so - Jokes Form',
            'time':str(datetime.now()),
        })
    )