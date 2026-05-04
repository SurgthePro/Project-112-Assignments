from django.contrib import admin
from .models import Post #Note: Post here begins with a Capital P because we are making reference to a class.

# Register your models here.
admin.site.register(Post)
