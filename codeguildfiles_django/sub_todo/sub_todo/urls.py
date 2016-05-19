"""sub_todo URL Configuration

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
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_index, name='index'),
    url(r'^add$', views.render_add_list, name='add_list'),
    url(r'^submit$', views.render_add_list_ack, name='add_list_submit'),
    url(r'^(?P<list_id>.+)/add$', views.render_list_add_item, name='add_item'),
    url(r'^(?P<list_id>.+)/add/submit$', views.render_add_item_ack, name='add_item_submit'),
    url(r'^(?P<list_id>.+)/(?P<item_id>.+)/delete$', views.render_delete_sub_item, name='delete_sub_item'),
]
