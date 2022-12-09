# Create your models here.
from django.db import models

class Conjunto(models.Model):
    conjunto = models.CharField(max_length=250)