from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here. Note: Only when changes are made here in this class object, do we need to make migrations and migrate.
class Post(models.Model):  # OOP  Object Oriented Programming: Where everything is stored in an object named Post. This object makes a reference to some memory address.
    title = models.CharField(max_length=128)  # similar to strings (There is no limit to max_length value.)
    subtitle = models.CharField(max_length=256)  # similar to strings-- each attribute has its own data type specified.
    body = models.TextField() # similar to strings
    created_on = models.DateTimeField(auto_now_add=True) # date / datetime
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # user data type--it means that it's making reference to another model (user). Since author will be making reference to a different table, we need to use a FK. The FK method requires two parameters: the model we want to refer to, the on_delete option--one of two options==the other option is DO_NOTHING (in case the model we are referring to gets deleted for some reason, all of their files also get deleted).

    def __str__(self): # This is similar to the JS method: toString() It takes this Post object and returns whatever we indicate here as a string. Otherwise, without this line of code, we just get the object #.
        return f"{self.id} - {self.title} by {self.author}"
    
    def get_absolute_url(self):  # Redirect a user wehn we execute a POST request.
        return reverse("post_detail", args=[self.id])
    
    
    

