from django.contrib import admin
from .models import Post, Status
             #Note: Post here begins with a Capital P because we are making reference to a class.

# Register your models here (after they are created in the database--file db.sqlite3).
admin.site.register([Post, Status])
