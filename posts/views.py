# from django.shortcuts import render          #Note: This file was automatically created when the posts app was created thru the cp terminal.
from django.views.generic import(ListView)
from .models import Post

# Create your views here.              # What this block of code does is (instead of just rendering a pure html that's just displaying data) gather data from the DB and sending that list to the templates (but the entire process doesn't stop there at templates, from the MVT model/diagram).
class PostListView(ListView):          #This is a new class we are creating here.  This is a class-based view/function. The ListView argument helps us to render a list of objects (posts in the table). The following three things listed here come from the ListView argument.
    template_name = "posts/list.html"  # template_name is the attribute used to render the html.
    model = Post                       # model variable/attribute lets django know from which model (table) we want to retrieve data.  It will render a Post object.
    context_object_name = "posts"      # context_object_name variable/attribute allows us to change the variable name on how we call it inside of templates.

