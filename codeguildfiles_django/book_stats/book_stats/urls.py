"""
Definition of urls for book_stats.
"""

from datetime import datetime
from django.conf.urls import patterns, url

from app import views

urlpatterns = [
    url(r'^$', views.render_count, name = 'count'),
    url(r'^count', views.render_count, name = 'count'),
]
