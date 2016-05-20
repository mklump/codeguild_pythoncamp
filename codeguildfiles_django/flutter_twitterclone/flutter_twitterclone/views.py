"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file flutter_twitterclone/views.py
by Matthew James K on 5/19/2016

Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from . import logic

def show_ten_latest(request):
    """
    Renders the home page.
    """
    assert isinstance(request, HttpRequest)
    found_fluts = None
    QUERY = request.GET['q'] if 'q' in request.GET else None
    search_by_user = request.GET['search_by_user'] if 'search_by_user' in request.GET else None
    if None == QUERY or None == search_by_user:
        found_fluts = logic.get_ten_latest_flutts()
    elif None != QUERY:
        found_fluts = logic.get_ten_fluts_by_query(QUERY)
    elif None != search_by_user:
        found_fluts = logic.get_ten_fluts_by_user(search_by_user)
    return render(
        request,
        'flutter_twitterclone/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Fluts Saved Here',
            'found_fluts':found_fluts,
        })
    )

def render_add_flut(request):
    """
    This view render function accepts a user name and a text string to add as a flut/tweet for the specifying user.
    """
    assert isinstance(request, HttpRequest)
    user_name = request.POST['user_name'] if 'user_name' in request.POST else None
    flut_text = request.POST['flut_text'] if 'flut_text' in request.POST else None
    if None == user_name or None == flut_text:
        response = HttpResponse(status = 400)
        return response.writelines('The save/post request for your user name, and for your flut text both cannot be empty.')
    else:
        flut_object = logic.save_submitted_user_flut_post(user_name, flut_text)
    return render(
        request,
        'flutter_twitterclone/acknowledgement.html',
        context_instance = RequestContext(request,
        {
            'title':'Your flut was saved',
            'user_name':flut_object.user_author,
            'flut_text':flut_object.text,
            'timestamp':flut_object.timestamp,
        })
    )