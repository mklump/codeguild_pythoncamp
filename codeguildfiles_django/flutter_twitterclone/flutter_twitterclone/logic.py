"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file flutter_twitterclone/logic.py
by Matthew James K on 5/19/2016
"""
from . import models
from django.db.models import Count
import datetime

def get_ten_latest_flutts():
    """
    This database function queries the database model and returns back the latest 10 flutt entries.
    :returns: a list [] of the latest ten flutt enties from the database.
    """
    models.User.objects.all()
    return models.Flut.objects.all().filter(user_author__user).order_by('timestamp')[:10]

def get_ten_fluts_by_query(query):
    """
    This database function queries the database model for 10 fluts having the specified text.
    :param 1: query is a string query for text to search for in the fluts presently persisted in the database.
    :returns: a string [] array that is the query result set of this data query
    """
    return models.Flut.objects.all().filter(text__contains = query).order_by('timestamp')[:10]

def get_ten_fluts_by_user(search_by_user):
    """
    This database function queries the database model for 10 fluts having the specified text.
    :param 1: query is a string query for text to search for in the fluts presently persisted in the database.
    :returns: a string [] array that is the query result set of this data query
    """
    return models.Flut.objects.all().filter(user_author = search_by_user).order_by('timestamp')[:10]

def get_user_by_id(id):
    """
    This database function queries the database model for one specific Flut, and returns the matching object,
    :returns: the one matching result query object by its id
    """
    return models.User.objects.all().filter(id=id)

def get_flut_by_id(id):
    """
    This database function queries the database model for one specific Flut, and returns the matching object,
    :returns: the one matching result query object by its id
    """
    return models.Flut.objects.all().filter(id=id)

def save_submitted_user_flut_post(user_name, flut_text):
    """
    This database function submits the posted data for the user and their associated flut text post with an auto time stamp.
    :param 1: user_name is a string representing the user who is saving this flut text post
    :param 2: flut_text is a string representing the user's flut text post
    :returns: the object model representing the flut details recently saved
    """
    user_object = models.User(user = user_name)
    flut_object = models.Flut(user_author = user_object, text = flut_text, timestamp = datetime.datetime.now())
    user_object.save()
    if None == flut_object.user_author_id: # attempt to explicitely assign to the foreign key, until I find a better way to handle this
        flut_object.user_author_id = 0;
    else:
        flut_object.user_author_id = flut_object.pk;
    flut_object.save()
    return flut_object