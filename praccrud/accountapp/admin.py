from django.contrib import admin

from .models import MyUser, BlogItem


admin.site.register(MyUser)
admin.site.register(BlogItem)