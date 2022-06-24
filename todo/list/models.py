from django.db import models

# Create your models here.

class List(models.Model):

    content = models.TextField()
    # completed = models.BooleanField(default=False)
    # incomplete = models.BooleanField(default=True)


    def __str__(self):
        
        return self.content 


