"""
    Python Coding Bootcamp (pdxcodeguild)
    Code File for web_madlib/views.py
    by: Erin Fough and Matthew James K on 5/9/2016
"""
from django.http import HttpResponse


def render_madlib_1(request):
    noun1 = request.GET['noun1']
    noun2 = request.GET['noun2']
    noun3 = request.GET['noun3']
    sentence = "{} hugged {} but not {}".format(noun1, noun2, noun3)
    response_positive = "200 OK"
    response_negative = "400 BAD REQUEST "
    if 'noun1' not in request.GET.items or \
       'noun2' not in request.GET.items or \
       'noun3' not in request.GET.items:
        return HttpResponse(status = 400, body = 'noun1, noun2, and noun3 post parameters are required');
    if noun1 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun1 was blank')
    elif noun2 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun2 was blank')
    elif noun3 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun3 was blank')
    else:
        return HttpResponse(status = 200, body = response_positive + ' ' + sentence)


def render_madlib_2(request):
    noun1 = request.GET['noun1']
    noun2 = request.GET['noun2']
    noun3 = request.GET['noun3']
    sentence = "{} troubled {} but not {}".format(noun1, noun2, noun3)
    response_positive = "200 OK"
    response_negative = "400 BAD REQUEST "
    if 'noun1' not in request.GET.keys or \
       'noun2' not in request.GET.keys or \
       'noun3' not in request.GET.keys:
        return HttpResponse(status = 400, body = 'noun1, noun2, and noun3 post parameters are required');
    if noun1 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun1 was blank')
    elif noun2 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun2 was blank')
    elif noun3 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun3 was blank')
    else:
        return HttpResponse(status = 200, body = response_positive + ' ' + sentence)


def render_madlib_3(request):
    noun1 = request.GET['noun1']
    noun2 = request.GET['noun2']
    noun3 = request.GET['noun3']
    sentence = "{} ran for {} but not {}".format(noun1, noun2, noun3)
    response_positive = "200 OK"
    response_negative = "400 BAD REQUEST "
    if 'noun1' not in request.GET.keys or \
       'noun2' not in request.GET.keys or \
       'noun3' not in request.GET.keys:
        return HttpResponse(status = 400, body = 'noun1, noun2, and noun3 post parameters are required');
    if noun1 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun1 was blank')
    elif noun2 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun2 was blank')
    elif noun3 == "":
        return HttpResponse(status = 400, body = response_negative + 'noun3 was blank')
    else:
        return HttpResponse(status = 200, body = response_positive + ' ' + sentence)