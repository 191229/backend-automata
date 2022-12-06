from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    first = models.CharField(max_length=1)
    second = models.CharField(max_length=1)
    three = models.CharField(max_length=1)
    fourth = models.CharField(max_length=1)