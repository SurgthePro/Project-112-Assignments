from django.urls import path
from .views import (HomePageView, AboutPageView, contact_me)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"), # This is an endpoint, except that we don't include the function portion--we only link the endpoint to the function, which is in another file. HomePageView is the name of the endpoint function that's in a different file (the views.py file)--so it needs to be imported.
    path("about/", AboutPageView.as_view(), name="about"), #This endpoint has a class-based view, so its formatting/syntax follows that type of view.  The view above it is also a class-based view. as_view() is a method. The third parameter is asking us to name the endpoint. So when the user enters the URL: http://127.0.0.1:8000/ they will open the home page.
    path("contact/", contact_me, name="contact"), # This endpoint has a function-based view (as was created on the file: views.py). We indicate the function name: contact_me, and we always need to add a name for the view.

]