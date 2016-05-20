"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file flutter_twitterclone/models.py
by Matthew James K on 5/19/2016

Definition of models.
"""

from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    """
    User class represnets a user with many fluts text posts.
    """
    user = models.TextField(unique = False, null = False)

    def __str__(self):
        return self.user

    def __repr__(self):
        return 'User(user={!r}'.format(self.user)

class Flut(models.Model):
    """
    Flut class represents a each new posting or tweet by a User.
    """
    user_author = models.ForeignKey(User, blank = False, null = False, on_delete=models.CASCADE)
    text = models.TextField(unique = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True, blank = False, unique = True, null = True)

    def __str__(self):
        return '{}, {}, {}'.format(self.user_author, self.text, self.timestamp)

    def __repr__(self):
        return 'Flut(user_author={!r}, text={!r}, timestamp={!r})'.format(self.user_author, self.text, self.timestamp)