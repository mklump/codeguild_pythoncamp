# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file <![CDATA[jokes/urls.py]]>
by Matthew James K on 5/12/2016

jokes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#from . import views
from . import ajax_view

urlpatterns = [
    #url(r'^$', views.render_index, name='index'), #not used
    #url(r'^form/submit$', views.submit_dry_dock_joke, name='submit'), #not used

    url(r'^admin/', admin.site.urls),
    url(r'^$', ajax_view.render_listing_index, name='index'),
    url(r'^ajax/$', ajax_view.render_listing_index, name = 'ajax_index'),
    url(r'^ajax/submit$', ajax_view.render_acknowledgement, name = 'joke_listing'),
]
