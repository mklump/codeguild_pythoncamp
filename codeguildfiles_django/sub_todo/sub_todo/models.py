from django.db import models

class List(models.Model):
    """docstring for List"""
    name = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'List(name={!r})'.format(self.name)


class ListItem(models.Model):
    """docstring for ListItem"""
    parent_list = models.ForeignKey(List)
    item = models.TextField()

    def __str__(self):
        return '{}, {}'.format(self.item, self.parent_list.name)

    def __repr__(self):
        return 'ListItem(item={!r}, parent={!r})'.format(self.item, self.parent_list.name)
