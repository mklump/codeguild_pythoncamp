"""
Definition of urls for flutter_twitterclone.
"""

from datetime import datetime
from django.conf.urls import url
from . import views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.show_ten_latest, name='home'),
    url(r'^USER_NAME/$', views.show_ten_latest, name='posts_by_user'),
    url(r'^post/$', views.render_add_flut, name='add_flut'),
    url(r'^post/submit/$', views.render_add_flut, name='post_submit'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
