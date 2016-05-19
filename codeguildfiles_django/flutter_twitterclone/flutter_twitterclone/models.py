"""
Definition of models.
"""

from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    """docstring for User"""
    user = models.TextField(unique = False, null = False)

    def __str__(self):
        return self.user

    def __repr__(self):
        return 'User(user={!r}'.format(self.user)

class Flut(models.Model):
    """
    Flut represents a each new posting or tweet by a User.
    """
    user_author = models.ForeignKey(User, unique = False, null = False)
    text = models.TextField(unique = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True, blank = False, unique = True, null = False)

    def __str__(self):
        return '{}, {}'.format(self.user_author, self.text)

    def __repr__(self):
        return 'Flut(user_author={!r}, text={!r}, timestamp={!r})'.format(self.user_author, self.text, self.timestamp)