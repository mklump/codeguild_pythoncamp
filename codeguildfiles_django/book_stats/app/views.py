"""
Python Coding Bootcamp (pdxcodeguild)
Code File for web_madlib/views.py
by: Matthew James K on 5/10/2016

Practice: Book Stats
1. Put your solution in a directory named book_stats.
It should be a full-fledged Django and Python application.
2. Make a "website" version of your word count practice.
No need to have the your site have HTML or CSS; just return raw text.
3. It should have one page that takes one argument that is the word you want the count for, /count?w=WORD.
Respond with a 200 OK code and a body containing WORD: COUNT. If the word doesn't exist in the book,
still respond with a 200 OK code but return a zero count in the body.
4. Place your word counting logic in a logic.py module in the application root.
(Feel free to copy your solution from before and strip out all of the UI functions.)
Have that module, on import load the word counts. Have your view functions from . import logic and call the counting functions.
Don't put the counting logic in the views.

Advanced
Make a second page / that presents an HTML form that lets the user enter a word.
Use events and jQuery's AJAX function to request the count for that word and dynamically update the page with the count.

Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

from . import logic

def render_count(request):
    response = None
    if 'w' not in request.GET or request.GET['w'] is '':
        response = HttpResponse(status = 400)
        response.write('400 BAD REQUEST - A word to count is expected in post parameter w.')
        return response
    else:
        word_to_count = request.GET['w']
        response = HttpResponse(status = 200)



#def home(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/index.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Home Page',
#            'year':datetime.now().year,
#        })
#    )

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        })
#    )

#def about(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/about.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'About',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        })
#    )
