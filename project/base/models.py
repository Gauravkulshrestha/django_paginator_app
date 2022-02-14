from pydoc import describe
from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=160)
    
    def __str__(self):
        return self.name