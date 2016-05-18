# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file jokes/ajax_view.py
by Matthew James K on 5/12/2016
"""
from django.shortcuts import render
from django.http import HttpResponse

from . import logic

def render_listing_index(request):
    """
    This view will render a listing of the joke and its associated punchline in a list format.
    :param 1: request is the incomming HttpRequest object from the urls.py page routes
    """
    all_jokes_data = logic.get_all_jokes_data()
    context = {
        'all_jokes_data':all_jokes_data
    }
    return render(request, 'no_jokes_here_only_dry/ajax_index.html', context)
    
def render_acknowledgement(request):
    """
    This view will accept POST for a joke and a punch line, and show an achnowledgement that the joke was saved.
    :param 1: request is the incomming HttpRequest object from the urls.py page routes
    """
    story_setup = request.GET['story_setup']
    punch_line = request.GET['punch_line']
    logic.ajax_save_submitted_joke(story_setup, punch_line)
    return HttpResponse('')