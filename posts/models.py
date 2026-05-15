from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here. Note: Only when changes are made here in this class object, do we need to make migrations and migrate.  Each class model on this pages/file, represents a different table.
class Status(models.Model):  #Here, we are creating a DB table called Status (Every table is connected to its app/folder, such as post.)  It's important to first create table and fill it wtih data--then create its relationship (foreign key).  This will be a Status table.
    class Meta:                                  # This code is only for cosmetic purposes.
        verbose_name_plural = "Status"

    name = models.CharField(max_length=128, unique=True)  #The name entered in the form should be unique--not repeated on other posts.
    description = models.CharField(max_length=200, help_text= "Write a description about the status.") # This text will appear in the mini Status form.

    def __str__(self):   # This is a string method, which makes the data readable.
        return f"{self.name}"     #After writing this code here, we need to create it on the database--so in the cp terminal, run the command: python manage.py makemigrations
    


class Post(models.Model):  # OOP  Object Oriented Programming: Where everything is stored in an object named Post. This object makes a reference to some memory address.
    title = models.CharField(max_length=128)  # similar to strings (There is no limit to max_length value.) This the leftmost column of a table in an SQL (relational) database.
    subtitle = models.CharField(max_length=256)  # similar to strings-- each attribute has its own data type specified.
    body = models.TextField() # similar to strings
    created_on = models.DateTimeField(auto_now_add=True) # date / datetime
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # user data type--it means that it's making reference to another model (user). Since author will be making reference to a different table, we need to use a FK. The FK method requires two parameters: the model we want to refer to, the on_delete option--one of two options==the other option is DO_NOTHING (in case the author we are referring to gets deleted for some reason, all of their files also get deleted).

    #options = models.CharField(max_length=20, choices=[
    #     ("draft", "option x"), 
    #     ("published", "option y"), 
    #     ("deleted", "option z")
    #     ])

    # Here, we are creating a foreign key for the status table:
    status= models.ForeignKey(Status, on_delete=models.DO_NOTHING) # This method receives two parameters: the first represents the relationship with another model/table, and the second has to do with the case that record (row data) is removed from the other table.

def __str__(self): # This is similar to the JS method: toString() It takes this Post object and returns whatever we indicate here as a string. Otherwise, without this line of code, we just get the object #.
        return f"{self.id} - {self.title} by {self.author}"
    
def get_absolute_url(self):  # Redirect a user when we execute a POST request
        return reverse("post_detail", args=[self.id])
    

    
    
    

