"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views (Function views are more flexible/manipulatable/powerful than class-based views, but they are more complicated.)
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #Include is a Django method

urlpatterns = [                      # To handle url routing in a Django application, we create url patterns in a list, and we attach different paths to those views--this is how Django knows which view to fire off when a user visits a url on our website.
    path('admin/', admin.site.urls), #This is the parent path, the other ones below this one are children. The order that the urls are placed here is the order they are executed when the server runs pages. Here, we can use the path() function, set a url route as its first argument, and assign an associated view--the admin method is a special argument here.
    path("", include("pages.urls")), #When we create urls inside other files, we need to register them here. We can put inside of url patterns, functions views, class-based views, or another url configuration (here, we are inserting the last type). The include() method serves to search our entire project for pages folder urls, which we will add here in this list. This is the parent, and the children are in the pages (url.py in the pages folder).
    path('posts/', include('posts.urls')), # Here, we are indicating that all the urls will will be creating begin with posts/ So all the children will have posts/ at the beginning (it's sort of like a lastname.) Example: posts/new or posts/list, etc.
]
