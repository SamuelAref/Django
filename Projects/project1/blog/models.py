from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls  import reverse


class Post(models.Model):

    title = models.CharField(max_length=100) #we set the blog title to a max length of 100 characters
    content = models.TextField() #content is a text field
    date_posted = models.DateTimeField(default=timezone.now) # the date posted here we imported the timezone so it will correspond, the we want it to make the date it was created 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # since user (author) is a different table, we access it by using a foreign key and importing a user from django above, the "CASCADE" refers to if the user is deleted then all the blogs will be deleted and not vice versa


    def __str__(self):

        return self.title

    
    def get_absolute_url(self):

        return reverse('post-detail', kwargs = {'pk': self.pk})

