from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here: Essentially, views are functions in charge of processing a user's request when they visit a certain url or endpoint on our website.  When a user goes to our website some view associated with that url is responsible for some logic in the back-end and returning some type of response with data--typically an html template or json data.
# Class-Based Views: classes use CamelCase for their names and arguments. Views can also be represented as classes. The main difference between the two types of views is how they extend logic.  Function-based views are easier to understand, it's important to understand both and how to use them.
class HomePageView(TemplateView): #This is the function name for the endpoint in the urls.py pages folder file.
    template_name = "pages/home.html" #This function renders a template (an html page). The variable: template_name belongs to the TemplateView parameter. It tells Django, that its value is where we want the html content loaded. That file (home.html) exists in the pages folder, which is nested inside the templates folder.

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

# Function-Based Views: functions (in Python) use snake_case syntax. Each function-based view requires a request. With the whole application process, everything starts with an HTTP request. But for class-based views, there's no need for requests.
def contact_me(request):
    #return HttpResponse("Hello World from a Function-Based View!") Function-based views always need to return something--an HTTP response.
    return render(request, "pages/contact.html") #This return is more practical.  Here we're using the render method that helps us build something from an html (what does that mean? I think it means we can display an html page that we created when the user enters the end url). We are passing a template name as an argument.

