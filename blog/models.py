from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)


# In Django, "dunder" is short for "double underscore," and it refers to methods and attributes in Python that have names starting and ending with double underscores. These methods are often called "magic methods" or "special methods." In the context of Django, dunder methods are used to customize the behavior of model instances and other objects.

# One prominent dunder method in Django is the __str__ method, which is used to define a human-readable representation of the object when it is printed or displayed. Here's an example in the context of a Django model:

    def __str__(self):
        return self.title