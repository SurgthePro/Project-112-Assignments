# from django.shortcuts import render          #Note: This file was automatically created when the posts app was created thru the cp terminal.
from django.views.generic import(ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin) # These are used for login & user authentication purposes. This is protect our endpoints in our views.
from .forms import PostForm
# Create your views here.              # What this block of code does is (instead of just rendering a pure html that's just displaying data) gather data from the DB and sending that list to the templates (but the entire process doesn't stop there at templates, from the MVT model/diagram).
class PostListView(ListView):          #This is a new class-based view we are creating here.  This is a class-based view/function. This view is implemented as a class.  We will be inheriting from an existing generic view function that already does most of what we want this view function to do, rather than writing our own from scratch.  For these views, we access an appropriate view function by calling the class method as_view() in the urls.py file.  Ths creates an instance of the class, which calls the appropriate handler methods for incoming HTTP requests.  The ListView argument helps us to render a list of objects (posts in the table). The following three things listed here come from the ListView argument. This is a GET request that returns a list.  This view is publically available.
    template_name = "posts/list.html"  # template_name is the attribute used to render the html.
    # model = Post 
    published_status = Status.objects.get(name="published")
    #queryset attribute allows us to select data from the db using the model class
    
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()
    # model variable/attribute lets django know from which model (table) we want to retrieve data.  It will render a Post object. This displays data from only one table.
    context_object_name = "posts"      # context_object_name variable/attribute allows us to change the variable name on how we call it inside of templates. (??? post_detail or post_list)

    def get_context_data(self, **kwargs):  #Note: These two lines of code (this and the one directly below) can be added below each of the other following four views, afther the corresponding class-based view (if you wish to modify their content).
        context = super().get_context_data(**kwargs)
       # print("before modifying context: \n{context}")
       # context["new_elements"] = "Hello, adding new value to the context"
        # print ("After modifying context \n{context}")
       # print(context)
        return context
class PostDetailView(LoginRequiredMixin, DetailView):    # This view needs to be protected/retricted for only memeber with an account. This is why we are including the first argument: LoginRequiredMixin. The order of the parameters here is important to consider--we put it first.  # GET request --> Single element (object)
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"      # This (context_object_name) is a relevant attribute of this generic view. (single_post is used in navbar.html and in detail.html)                                    # SELECT * FROM expenses WHERE id= # Note: This returns a single object element.

    def get_context_data(self, **kwargs):   # The get_context_data() function has to do with how we are passing our elements thru the various parts of the MVT (DJ system).   The context apparatus begins running as soon as our project starts running (context is a part of a dictionary).  Each element can be found in each class that we have in the views.py file.
        context = super().get_context_data(**kwargs) #kwargs tells the function that it's being passed to that it can hold not only single values, but multiple values, such as lists, tuples, or dictionaries, or objects (if we only include a single asterisk, that means this function can only recieve single values).  
        # print("before modifying context: \n{context}")
        context["message"] = "You need to login before you can view the post content details."  # Here, we need to add code in the template html file so that this message can display.
        # print ("After modifying context \n{context}")
        # print(context)
        return context

class PostCreateView(LoginRequiredMixin, CreateView):            # POST request --> empty form on HTML
    template_name = "posts/new.html"
    model = Post
    # Fields attribute is a list that allows us to enable/disable the inputs to render in the html.
    
    # form_class = PostForm
    fields = ["title", "subtitle", "body", "status"]  # These are the fields of the db table.

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    success_url = "/posts/"
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # This view requires additonal authentication bc we only want the post creator/author to update his post (also refer to code lines 40 to 48.).  #POST request --> filled form html
    template_name = "posts/edit.html"          # This (template_name) is a relevant attribute of this generic view.
    model = Post                               # This (model) is a relevent attribute of this generic (class-based) view.
    fields = ["title", "subtitle", "body", "status"]     # This (fields) is a relevant attribute of generic view.

    def test_func(self):                       # This function code supports the UserPassesTestMixin parameter (this is the function test that needs to return True).
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False
        
    success_url = "/posts/"
        # print(f"Printing post: {post}")
        # print(f"Printing request: {self.request}")
        # print(f"Printing self: {self}")
        # return True
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):   # This view requires additonal authentication bc we only want the post creator/author to delete his post (also refer to code lines 68 to 76).       # POST Request 
    template_name = "posts/delete.html"
    model = Post
    # success_url attribute allows us to redirect the user if the request was successful.
    success_url = reverse_lazy("post_list")    # This (success_url) is a relevant attribute of this generic view.

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:  # This means that the user is the author, then they are granted access.
                return True
            else:
                return False
        else:
            return False
        
class PostArchivedListView(ListView): #This inherits from the generic class--ListView
    template_name = "posts/list.html"  #Here, we use the same value as the generic/parent class.
    archived_status = Status.objects.get(name="archived")  #This means ???  But it needs to placed before queryset.
    context_object_name = "posts"      #Here, we use the same value as the generic/parent class.
    queryset = Post.objects.filter(status=archived_status).order_by("created_on").reverse() #Note: Some of these attributes listed here in this class-based view need to be placed before others, otherwise there will be issues.

class PostDraftListView(ListView):
    template_name = "posts/list.html"
    draft_status = Status.objects.get(name="draft")
    context_object_name = "posts"
    # queryset = Post.objects.filter(status=archived_status).order_by("created_on").reverse() Note: The code snippet below can substitute for this--just an alternate way to get to the queryset.

    def get_queryset(self):
        draft_status = Status.objects.get(name="draft")
        return Post.objects.filter(status=draft_status)

    
        
