"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file flutter_twitterclone/views.py
by Matthew James K on 5/19/2016

Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from . import logic

def show_ten_latest(request):
    """
    Renders the home page.
    """
    assert isinstance(request, HttpRequest)
    found_fluts = None
    QUERY = request.GET['q'] if 'q' in request.GET else None
    if None == QUERY:
        found_fluts = logic.get_ten_latest_flutts()
    else:
        found_fluts = logic.get_ten_fluts_by_query(QUERY)
    return render(
        request,
        'flutter_twitterclone/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Flutts Saved Here',
            'found_fluts':found_fluts,
        })
    )

def render_add_flut(request):
    """
    This view render function accepts a user name and a text string to add as a flut/tweet for the specifying user.
    """
    assert isinstance(request, HttpRequest)
