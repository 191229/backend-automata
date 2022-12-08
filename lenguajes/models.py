# Create your models here.
from django.db import models

class Post(models.Model):
    first = models.CharField(null=False, max_length=250)