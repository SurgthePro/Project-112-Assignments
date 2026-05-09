from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  #This is needed to be able to create a signup (create account) form.
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView): # POST request; the CreateView parameter tells the function more specifically what to create.
    template_name = "registration/signup.html"  # This code indicates where the file is so that DJ can find it and then render it.

    # We use this one when we want to have a custom form.
    form_class = UserCreationForm    # form_class attribute allows us to create ojbects from a form. UserCreationForm is a specific type of form.
    success_url = reverse_lazy("login") # This code line does two things: gives a confirmation message and redirects the user to the login page.

