# from django.shortcuts import render          #Note: This file was automatically created when the posts app was created thru the cp terminal.
from django.views.generic import(ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.              # What this block of code does is (instead of just rendering a pure html that's just displaying data) gather data from the DB and sending that list to the templates (but the entire process doesn't stop there at templates, from the MVT model/diagram).
class PostListView(ListView):          #This is a new class we are creating here.  This is a class-based view/function. The ListView argument helps us to render a list of objects (posts in the table). The following three things listed here come from the ListView argument. This is a GET request that returns a list.
    template_name = "posts/list.html"  # template_name is the attribute used to render the html.
    model = Post                       # model variable/attribute lets django know from which model (table) we want to retrieve data.  It will render a Post object. This displays data from only one table.
    context_object_name = "posts"      # context_object_name variable/attribute allows us to change the variable name on how we call it inside of templates.

class PostDetailView(DetailView):      # GET request --> Single element (object)
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"      # This (context_object_name) is a relevant attribute of this generic view.

                                             # SELECT * FROM expenses WHERE id= # Note: This returns a single object element.
class PostCreateView(CreateView):            # POST request --> empty form on HTML
    template_name = "posts/new.html"
    model = Post
    # Fields attribute is a list that allows us to enable/disable the inputs to render in the html.
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView): #POST request --> filled form html
    template_name = "posts/edit.html"          # This (template_name) is a relevant attribute of this generic view.
    model = Post                               # This (model) is a relevent attribute of this generic (class-based) view.
    fields = ["title", "subtitle", "body"]     # This (fields) is a relevant attribute of this generic view.

class PostDeleteView(DeleteView):          # POST Request 
    template_name = "posts/delete.html"
    model = Post
    # success_url attribute allows us to redirect the user if the request was successful.
    success_url = reverse_lazy("post_list")    # This (success_url) is a relevant attribute of this generic view.


