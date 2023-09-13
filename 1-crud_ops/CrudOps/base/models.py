from django.db import models

# Create your models here.


class Person(models.Model):
    """A class with two fields -> person name and ID"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
