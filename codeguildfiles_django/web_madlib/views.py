"""
    Python Coding Bootcamp (pdxcodeguild)
    Code File for web_madlib/views.py
    by: Erin Fough and Matthew James K on 5/9/2016
"""
from django.http import HttpResponse


def get_httpresponse_to_request(request = [], sentence = ''):
    """
    This function accepts the sentence for each numbered request, and the request object, and gives back the HttpResponse
    :param 1: request is the [] Array of the current incommng http request post parameters from the client
    :param 2: sentence is the main body of the madlib string as a String
    :returns: the HttpResponse for each of the ^1 url incomming requests.
    """
    response_positive = "200 OK"
    response_negative = "400 BAD REQUEST "
    if request[0] is None or request[0] is '':
        response = HttpResponse(status = 400)
        response.write(response_negative + 'noun1 was not provided or blank')
        return response
    elif request[1] is None or request[1] is '':
        response = HttpResponse(status = 400)
        response.write(response_negative + 'noun2 was not provided or blank')
        return response
    elif request[2] is None or request[2] is '':
        response = HttpResponse(status = 400)
        response.write(response_negative + 'noun3 was not provided or blank')
        return response
    else:
        response = HttpResponse(status = 200)
        response.write(response_positive + ' ' + sentence)
        return response


def render_madlib_1(request):
    post_parameters = []
    post_parameters.append(request.GET['noun1'] if 'noun1' in request.GET else None) #The key value must be accessible
    post_parameters.append(request.GET['noun2'] if 'noun2' in request.GET else None) #If the in expression does not work, use request.GET.get() then check for None
    post_parameters.append(request.GET['noun3'] if 'noun3' in request.GET else None)
    sentence = "{} hugged {} but not {}".format(post_parameters[0], post_parameters[1], post_parameters[2])
    return get_httpresponse_to_request(post_parameters, sentence)


def render_madlib_2(request):
    post_parameters = []
    post_parameters.append(request.GET['noun1'] if 'noun1' in request.GET else None)
    post_parameters.append(request.GET['noun2'] if 'noun2' in request.GET else None)
    post_parameters.append(request.GET['noun3'] if 'noun3' in request.GET else None)
    sentence = "{} troubled {} but not {}".format(post_parameters[0], post_parameters[1], post_parameters[2])
    return get_httpresponse_to_request(post_parameters, sentence)


def render_madlib_3(request):
    post_parameters = []
    post_parameters.append(request.GET['noun1'] if 'noun1' in request.GET else None)
    post_parameters.append(request.GET['noun2'] if 'noun2' in request.GET else None)
    post_parameters.append(request.GET['noun3'] if 'noun3' in request.GET else None)
    sentence = "{} ran for {} but not {}".format(post_parameters[0], post_parameters[1], post_parameters[2])
    return get_httpresponse_to_request(post_parameters, sentence)