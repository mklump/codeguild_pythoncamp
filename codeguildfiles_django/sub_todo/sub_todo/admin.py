from django.contrib import admin
from sub_todo import models

admin.site.register(models.List)
admin.site.register(models.ListItem)
