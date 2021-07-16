from django.db import models
from django.db.models.base import Model

# Create your models here.
class Blogs(models.Model):
    post  = models.TextField(max_length=1000)
    name  = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
