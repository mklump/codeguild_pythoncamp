"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file flutter_twitterclone/logic.py
by Matthew James K on 5/19/2016
"""
from . import models
from django.db.models import Count

def get_ten_latest_flutts():
    """
    This database function queries the database model and returns back the latest 10 flutt entries.
    :returns: a list [] of the latest ten flutt enties from the database.
    """
    return models.Flut.objects.all().order_by('timestamp')[:10]

def get_ten_fluts_by_query(query):
    """
    This database function queries the database model for 10 fluts having the specified text.
    :param 1: query is a string query for text to search for in the fluts presently persisted in the database.
    :returns: a string [] array that is the query result set of this data query
    """
    return models.Flut.objects.all().filter(text__contains='query').order_by('timestamp')[:10]

